import unittest
from src.app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)
        # Test that course names are displayed
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Data Science Fundamentals', response.data)
        self.assertIn(b'Go Programming Essentials', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_golang_course(self):
        response = self.app.get('/course/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go Programming Essentials', response.data)
        self.assertIn(b'Robert Chen', response.data)

if __name__ == '__main__':
    unittest.main()