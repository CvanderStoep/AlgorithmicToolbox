# python3

from random import randint


def partition3(array, lo, hi):
    # <v  =v  >v
    x = array[lo]
    lt = lo
    gt = hi
    i = lo
    while i <= gt:
        number = array[i]
        if number < x:
            array[i], array[lt] = array[lt], array[i]
            lt += 1
            i += 1
        if number > x:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
        if number == x:
            i += 1
    return lt, gt


def partition2(array, left, right):
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[left], array[j] = array[j], array[left]
    return j


def randomized_quick_sort(array, left, right):
    if left >= right:
        return

    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    # code voor Partition
    # m = partition2(array, left, right)
    # randomized_quick_sort(array, left, m - 1)
    # randomized_quick_sort(array, m + 1, right)
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
