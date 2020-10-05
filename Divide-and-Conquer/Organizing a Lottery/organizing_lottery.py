# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

#less naive, but still O(n^2)
def points_cover(starts, ends, points):
    segments = []
    for start, end in zip(starts, ends):
        segments.append([start, end])
    segments.sort()

    count = [0] * len(points)
    for index, point in enumerate(points):
        for segment in segments:
            start = segment[0]
            end = segment[1]
            # print(segment, start, end)
            if point < start:
                break
            if start <= point <= end:
                count[index] += 1

    return count

#start list of all start/end/points and keep running count
#O(n log n)
def points_cover2(starts, ends, points):
    array_list = []
    count = [0] * len(points)

    for start in starts:
        array_list.append([start, "l"])
    for end in ends:
        array_list.append([end, "r"])
    for index, point in enumerate(points):
        array_list.append([point, "p", index])
    array_list.sort()

    running_count = 0
    while len(array_list) != 0:
        element = array_list.pop(0)
        if element[1] == "l":
            running_count += 1
        if element[1] == "r":
            running_count -= 1
        if element[1] == "p":
            count[element[2]] = running_count

    return count


if __name__ == '__main__':
    # data = list(map(int, stdin.read().split()))
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
    output_count = points_cover2(input_starts, input_ends, input_points)
    print(*output_count)
