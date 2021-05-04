from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course, CourseSchema

# Connect to Database and create database session
engine = create_engine('sqlite:///usr/local/WB/data/course-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)


# landing page that will display all the books in our database
# This function operate on the Read operation.
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



















# This will let us Create a new book and save it in our database
@app.route('/courses/new/', methods=['GET', 'POST'])
def newCourse():
    if request.method == 'POST':
        newCourse = Course(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(newCourse)
        session.commit()
        return str("NEW")
    else:
        return str("NEW")


# This will let us Update our books and save it in our database
@app.route("/courses/<int:course_id>/edit/", methods=['GET', 'POST'])
def editBook(course_id):
    editedCourse = session.query(Course).filter_by(id=course_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCourse.title = request.form['name']
            return str("ONE")
    else:
        return str("ONE")


# This will let us Delete our book
@app.route('/courses/<int:course_id>/delete/', methods=['GET', 'POST'])
def deleteBook(course_id):
    courseToDelete = session.query(Course).filter_by(id=course_id).one()
    if request.method == 'POST':
        session.delete(courseToDelete)
        session.commit()
        return str("delete")
    else:
        return str("delete")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
