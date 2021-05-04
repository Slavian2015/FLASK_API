from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course
from sqlalchemy.ext.serializer import loads, dumps

import decimal
import datetime


def alchemy_encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

import json
from sqlalchemy import text


# Connect to Database and create database session
engine = create_engine('sqlite:///usr/local/WB/data/course-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# one_weeks = datetime.datetime.now() + timedelta(days=7)
# two_weeks = datetime.datetime.now() + timedelta(days=14)
#
#
# bookOne = Course(title="Math", start_date=datetime.datetime.now(), end_date=one_weeks, amount=45)
# bookTwo = Course(title="Literature", start_date=datetime.datetime.now(), end_date=one_weeks, amount=55)
# bookThree = Course(title="Art", start_date=datetime.datetime.now(), end_date=two_weeks, amount=30)
#
# session.add(bookOne)
# session.commit()
#
# session.add(bookTwo)
# session.commit()
#
# session.add(bookThree)
# session.commit()


courses = session.query(Course).all()
res = json.loads(json.dumps([dict(r) for r in courses], default=alchemy_encoder))


print("ALL :\n", res)