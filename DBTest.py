from sqlalchemy import create_engine
from tokens import POSTGRES_CONNECTION_STRING
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime
import datetime

engine = create_engine(POSTGRES_CONNECTION_STRING, echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True) 
    searchTerm = Column(String)
    result = Column(String)
    datetime = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self): 
        return "<Query(searchTerm='%', result='%s', datetime='%s')" % (self.searchTerm, self.result, self.datetime)


def fill_table():
    Base.metadata.create_all(engine)
    session.add_all([
        Query(searchTerm="Cheese", result="76"),
        Query(searchTerm="Burger", result="86"),
        Query(searchTerm="Sandwich", result="96")
    ])

    print session.dirty
    print session.dirty 

    session.commit()

def view_table(): 
    for row in session.query(Query).all():
        print (row.searchTerm, row.result)

