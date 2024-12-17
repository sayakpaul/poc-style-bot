import math
import unittest

from poc_style_bot import circle_area, circle_circumference


class TestCircleFunctions(unittest.TestCase):
    def test_circle_area(self):
        # Test area with a unit radius
        self.assertAlmostEqual(circle_area(1), math.pi)

        # Test area with zero radius
        self.assertAlmostEqual(circle_area(0), 0.0)

        # Test area with a fractional radius
        radius = 2.5
        expected = math.pi * radius**2
        self.assertAlmostEqual(circle_area(radius), expected)

        # Test with a large radius
        radius = 100
        expected = math.pi * (100**2)
        self.assertAlmostEqual(circle_area(radius), expected)

    def test_circle_circumference(self):
        # Test circumference with a unit radius
        self.assertAlmostEqual(circle_circumference(1), 2 * math.pi)

        # Test circumference with zero radius
        self.assertAlmostEqual(circle_circumference(0), 0.0)

        # Test circumference with a fractional radius
        radius = 2.5
        expected = 2 * math.pi * radius
        self.assertAlmostEqual(circle_circumference(radius), expected)

        # Test with a large radius
        radius = 100
        expected = 2 * math.pi * 100
        self.assertAlmostEqual(circle_circumference(radius), expected)
