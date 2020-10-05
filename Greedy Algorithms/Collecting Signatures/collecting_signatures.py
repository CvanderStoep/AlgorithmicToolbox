# python3

from collections import namedtuple
from sys import stdin
from copy import deepcopy

Segment = namedtuple('Segment', 'start end')
Ship = namedtuple('Ship', 'company location')


def compute_optimal_points(segments):
    print(segments)
    list_of_overlapping_points = []

    while len(segments) != 0:
        first_finish = 1000000
        for segment in segments:
            if segment.end < first_finish:
                first_finish = segment.end
        print('first_finish= ', first_finish)
        list_of_overlapping_points.append(first_finish)
        # TODO use sorted list

        copy_segments = deepcopy(segments)
        for segment in segments:
            if segment.start <= first_finish:
                copy_segments.remove(segment)  # remove segment
        segments = deepcopy(copy_segments)

    return list_of_overlapping_points


if __name__ == '__main__':
    # n, *data = map(int, stdin.read().split())
    n, *data = map(int, input().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[0::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    ship = Ship('bedrijfA', 100)
    ship = ship._replace(location=50)
    print(ship)
    print(len(output_points))
    print(*output_points)
