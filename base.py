# B"H

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# example using postgres database called 'powersystem'
db_uri = 'postgresql://postgres:postgres@localhost:5432/powersystem'
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)

Base = declarative_base()
