import unittest
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from random import randint


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
                [Point(1, 0), Point(1, 1)],
                [Point(1, 2), Point(3, 4)],
                [Point(1, 0), Point(-1, 1), Point(1, 0), Point(1, 0), Point(-1, -1)]
        ):
            self.assertAlmostEqual(minimum_distance_squared(points),
                                   minimum_distance_squared_naive(points),
                                   delta=1e-03)

    def test_random(self):
        for n in [2, 5, 10, 1000]:
            for max_value in [1, 2, 3, 1000]:
                points = []
                for _ in range(n):
                    x = randint(-max_value, max_value)
                    y = randint(-max_value, max_value)
                    points.append(Point(x, y))

                # minimum_distance_squared(points)
                # minimum_distance_squared_naive(points)
                self.assertAlmostEqual(minimum_distance_squared(points),
                                       minimum_distance_squared_naive(points),
                                       delta=1e-03)

    # def test_large(self):
    #     type here


if __name__ == '__main__':
    unittest.main()
