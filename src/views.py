from flask import render_template
from models import Course

def index():
    return render_template('index.html')

def course(course_id):
    course = Course.get(course_id)
    return render_template('course.html', course=course)

def contact():
    return render_template('contact.html')