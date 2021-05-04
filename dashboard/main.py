from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course, CourseSchema
import datetime

# Connect to Database and create database session
engine = create_engine('sqlite:///usr/local/WB/data/course-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


@app.route('/')
@app.route('/courses')
def show_courses():
    courses = session.query(Course).all()
    result = courses_schema.dump(courses)
    return jsonify(result)


# This will let us Show one course
@app.route('/courses/<int:course_id>', methods=['GET'])
def show_course(course_id):
    course_to_show = session.query(Course).get(course_id)
    return course_schema.jsonify(course_to_show)


# This will let us FIND one course by Title / start_date / end_date
@app.route('/courses/find', methods=['POST'])
def find_course():
    if "title" in request.json.keys():
        course_to_find = session.query(Course).filter_by(title=request.json["title"]).first()
        return course_schema.jsonify(course_to_find)
    elif "start_date" in request.json.keys():
        year, month, day = request.json['start_date'].split('-')
        course_to_find = session.query(Course).filter(Course.start_date >= datetime.date(int(year), int(month), int(day)))
        return courses_schema.jsonify(course_to_find)
    elif "end_date" in request.json.keys():
        year, month, day = request.json['end_date'].split('-')
        course_to_find = session.query(Course).filter(Course.end_date >= datetime.date(int(year), int(month), int(day)))
        return courses_schema.jsonify(course_to_find)
    else:
        return {"error": "No title to find"}


# This will let us to UPDATE one course
@app.route('/courses/<int:course_id>', methods=["PUT"])
def course_update(course_id):
    course_to_update = session.query(Course).get(course_id)

    for i in request.json.keys():
        if i == 'title':
            course_to_update.title = request.json[i]
        elif i == 'start_date':
            course_to_update.start_date = request.json[i]
        elif i == 'end_date':
            course_to_update.end_date = request.json[i]
        elif i == 'amount':
            course_to_update.amount = request.json[i]

    session.commit()
    return course_schema.jsonify(course_to_update)


# This will let us DELETE course by Id
@app.route('/courses/<int:course_id>', methods=["DELETE"])
def user_delete(course_id):
    try:
        course_to_delete = session.query(Course).filter_by(id=course_id).one()
        session.delete(course_to_delete)
        session.commit()
        return course_schema.jsonify(course_to_delete)
    except exc.SQLAlchemyError:
        return {"error": "No such Id"}


# This will let us Create a new course and save it in our database
@app.route('/courses/new', methods=['POST'])
def new_course():

    format_date = "%Y-%m-%d"
    if all(item in request.json.keys() for item in ["title", "start_date", "end_date", "amount"]):
        try:
            new_course_item = Course(title=request.json['title'],
                                     start_date=datetime.datetime.strptime(request.json['start_date'], format_date),
                                     end_date=datetime.datetime.strptime(request.json['end_date'], format_date),
                                     amount=request.json['amount'])
            session.add(new_course_item)
            session.commit()
            courses = session.query(Course).all()
            result = courses_schema.dump(courses)
            return jsonify(result)
        except exc.SQLAlchemyError:
            return {"error": "Incorrect value. Please try another"}
    else:
        return {"error": "Not all values are present"}


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
