#Joseph Letizia
#SSW 567
#HW 01: Testing Triangle Classification

import unittest
from triangles import classify_triangle

class test_triangles(unittest.TestCase):

    def test_validation0(self):
        self.assertEqual(classify_triangle("a", 4, 5), "An input(s) is not valid")
        self.assertEqual(classify_triangle(3, 4, "b"), "An input(s) is not valid")

    def test_validation1(self):
        self.assertEqual (classify_triangle(0, 4, 5), "Invalid Triangle")
        self.assertEqual (classify_triangle(3, 0, 5), "Invalid Triangle")

    def test_validation2(self):
        self.assertEqual (classify_triangle(5, 5, 102), "Invalid Triangle")
        self.assertEqual (classify_triangle(4, 200, 3), "Invalid Triangle")

    def test_equilateral(self):
        self.assertEqual (classify_triangle(3, 3, 3), "Equlateral Triangle")
        self.assertEqual (classify_triangle(9, 9, 9), "Equlateral Triangle")

    def test_isosceles(self):
        self.assertEqual (classify_triangle(4, 4, 7), "Isosceles Triangle")
        self.assertEqual (classify_triangle(5, 5, 9), "Isosceles Triangle")

    def test_right_scalene(self):
        self.assertEqual (classify_triangle(5, 12, 13), "Right and Scalene Triangle")
        self.assertEqual (classify_triangle(3, 4, 5), "Right and Scalene Triangle")

    def test_scalene(self):
        self.assertEqual (classify_triangle(4, 6, 9), "Scalene Triangle")
        self.assertEqual (classify_triangle(14, 16, 28), "Scalene Triangle")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)