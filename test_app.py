import unittest
import app

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(4, 4), 9)

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(app.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(app.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
