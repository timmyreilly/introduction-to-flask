#app.py 
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/formed', methods=['GET', 'POST'])
def formed():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        session['name'] = form.name.data
        return redirect(url_for('formed'))
    return render_template('formed.html', form=form, name=session.get('name'))

if __name__ == "__main__":
    app.run(debug=True)