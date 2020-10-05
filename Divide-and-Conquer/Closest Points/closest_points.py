# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):
    min_distance_squared = float("inf")

    if len(points) < 2:
        return float("inf")
    if len(points) == 2:
        p1 = points[0]
        p2 = points[1]
        return distance_squared(p1, p2)
    else:
        x_min = min(points, key=lambda k: k.x).x
        x_max = max(points, key=lambda k: k.x).x
        x_half = x_min + (x_max - x_min) / 2
        S1 = []
        S2 = []
        left = True
        for p in points:
            if p.x < x_half:
                S1.append(p)
            if p.x > x_half:
                S2.append(p)
            if p.x == x_half: #divide points on x_half axis 50/50%
                if left:
                    S1.append(p)
                else:
                    S2.append(p)
                left = not left
        d1 = minimum_distance_squared(S1)
        d2 = minimum_distance_squared(S2)
        d = min(d1, d2)

        #Inspect strip around x_half +/- d
        Strip = []
        for p in points:
            if x_half - d < p.x < x_half + d:
                Strip.append(p)
        #TODO use better algoritme than naive for the strip
        d_strip = minimum_distance_squared_naive(Strip)
        d = min(d, d_strip)
        return d


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print(input_points)

    print("{0:.4f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    print("{0:.5f}".format(sqrt(minimum_distance_squared(input_points))))
