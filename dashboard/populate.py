from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

from database_setup import Course, Base

engine = create_engine('sqlite:///usr/local/WB/data/course-collection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()


one_weeks = datetime.now() + timedelta(days=7)
two_weeks = datetime.now() + timedelta(days=14)


bookOne = Course(title="Math", start_date=datetime.now(), end_date=one_weeks, amount=45)
bookTwo = Course(title="Literature", start_date=datetime.now(), end_date=one_weeks, amount=55)
bookThree = Course(title="Art", start_date=datetime.now(), end_date=two_weeks, amount=30)

session.add(bookOne)
session.commit()

session.add(bookTwo)
session.commit()

session.add(bookThree)
session.commit()



