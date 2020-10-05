# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    [A, n] = MergeSort(a)

    return n


def MergeSort(A):
    n = len(A)
    n_inversions = 0
    if n == 1:
        return [A, 0]
    m = n // 2
    [B, n_ib] = MergeSort(A[:m])  # [0-m)
    [C, n_ic] = MergeSort(A[m:])  # [m-n]
    [A, n_i] = Merge(B, C)
    n_inversions = n_inversions + n_i + n_ib + n_ic
    return [A, n_inversions]


def Merge(B, C):
    D = []
    n_inversions = 0
    while len(B) != 0 and len(C) != 0:
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
            n_inversions += len(B)
    while len(B) != 0:
        D.append(B.pop(0)) #empty array B
    while len(C) != 0:
        D.append(C.pop(0)) #empty array C
    return [D, n_inversions]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions_naive(elements))
    print(compute_inversions(elements))
    print(MergeSort(elements))
