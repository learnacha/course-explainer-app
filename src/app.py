from flask import Flask
from views import index, course

app = Flask(__name__)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/course/<int:course_id>', 'course', course)

if __name__ == '__main__':
    app.run(debug=True)