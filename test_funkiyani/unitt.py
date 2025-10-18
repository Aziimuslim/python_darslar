import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
 def test_area(self):
  self.assertEqual(getArea(5), 78.53975)
  self.assertEqual(getArea(10), 314.159)
unittest.main()

