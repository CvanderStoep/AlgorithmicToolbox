import unittest
from organizing_lottery import points_cover, points_cover_naive, points_cover2
from random import randint


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 5], [7, 10], [1, 6, 11, 3, 5, 2, 5])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))
            self.assertEqual(points_cover([0, 5], [7, 10], [1, 6, 11]), [1, 2, 0])
            self.assertEqual(points_cover([-10, -8, 1, 2], [1, 1, 4, 5], [-11, -10, -9, -8, -7, -5, 0]),
                             [0, 1, 1, 2, 2, 2, 2])

    def test_random(self):
        n = 500
        starts = []
        ends = []
        points = []
        for _ in range(n):
            start = randint(0, 100)
            length = randint(0, 100)
            end = start + length
            point = randint(-200, 200)
            starts.append(start)
            ends.append(end)
            points.append(point)

        points_cover2(starts, ends, points)
        self.assertEqual(points_cover2(list(starts), list(ends), list(points)),
                         points_cover_naive(starts, ends, points))

    # def test_random(self):
    #     type here
    #
    # def test_large(self):
    #     type here


if __name__ == '__main__':
    unittest.main()
