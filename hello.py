#app.py 
from flask import Flask, render_template, session, redirect, url_for 
from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField
from flask.ext.bootstrap import Bootstrap
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import datetime
from tokens import POSTGRES_CONNECTION_STRING 
from wiki_sentiment import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_CONNECTION_STRING
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Query(db.Model):
    __tablename__ = 'queries'

    id = db.Column(db.Integer, primary_key=True) 
    searchTerm = db.Column(db.String)
    result = db.Column(db.String)
    datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    def add(self, query):
        db.session.add(query)
        return db.session.commit() 

    def __repr__(self): 
        return json.dumps("{'searchTerm':'%s', 'result':'%s', 'datetime':'%s'}" % (self.searchTerm, self.result, self.datetime))

class SearchForm(Form):
    searchterm = StringField('What Wikipedia article would you like to analyze?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route("/resume")
def hello():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        session['searchterm'] = form.searchterm.data 
        session['sentiment'], session['titlearticle'], session['wikiurl'] = get_sentiment_from_url(get_one_url_from_wiki_search(session.get('searchterm')))
        return redirect(url_for('search'))
    return render_template('search.html', form=form, searchterm=session.get('searchterm'), number=session.get('sentiment'), titlearticle=session.get('titlearticle'), wikiUrl=session.get('wikiurl'))


@app.route('/useDB', methods=['GET', 'POST'])
def useDB():
    form = SearchForm()
    allQueries = Query.query.all() 
    if form.validate_on_submit():
        # put the content of the query in the session
        session['searchterm'] = form.searchterm.data
        session['sentiment'], session['titlearticle'], session['wikiurl'] = get_sentiment_from_url(get_one_url_from_wiki_search(session.get('searchterm')))
        
        # grab the session info and put it in the db 
        q = Query(searchTerm=session['titlearticle'], result=session['sentiment'])
        query_add = q.add(q)

        return redirect(url_for('useDB'))
    return render_template('useDB.html', queries=allQueries, form=form, searchterm=session.get('searchterm'), number=session.get('sentiment'), titlearticle=session.get('titlearticle'), wikiUrl=session.get('wikiurl')  )

if __name__ == "__main__":
    app.run(debug=True)