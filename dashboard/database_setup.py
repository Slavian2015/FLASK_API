import sys
# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
import os

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine
from flask_marshmallow import Marshmallow

# create declarative_base instance
Base = declarative_base()
ma = Marshmallow()


# we'll add classes here
class Course(Base):
    __tablename__ = 'course'

    id = Column('course_id', Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'start_date', 'end_date', 'amount')


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///usr/local/WB/data/course-collection.db')

Base.metadata.create_all(engine)
