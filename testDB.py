from tokens import POSTGRES_CONNECTION_STRING as PCS 

print PCS # should look like: postgresql://postgres:password@40.83.182.555/mydb 

from sqlalchemy import Table, Column, Integer, String, ForeignKey

import sqlalchemy

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

def connectLazy(): 
    con = sqlalchemy.create_engine(PCS, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta 

con, meta = connect('federer', 'grandestslam', 'sentiment', '40.83.182.130')

slams = Table('slams', meta, 
    Column('name', String, primary_key=True),
    Column('country', String)
)

searches = Table('')

results = Table('results', meta, 
    Column('slam', String, ForeignKey('slams.name')),
    Column('year', Integer), 
    Column('result', String)
)

meta.create_all(con) 