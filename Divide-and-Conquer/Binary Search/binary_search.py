# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    # call the actual BS algorithm
    return BinarySearch(keys, 0, len(keys) - 1, query)


def BinarySearch(A, low, high, key):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if A[mid] == key:
        return mid
    else:
        if key < A[mid]:
            return BinarySearch(A, low, mid - 1, key)
        else:
            return BinarySearch(A, mid + 1, high, key)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
