class Course:
    def __init__(self, title, description, instructor, duration):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

    @staticmethod
    def get(course_id):
        try:
            return courses[int(course_id) - 1]
        except (ValueError, IndexError):
            return None

courses = [
    Course("Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks"),
    Course("Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks"),
    Course("Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks"),
]