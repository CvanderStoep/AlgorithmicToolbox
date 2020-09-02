# python3
# import numpy as np
l1, l2, l3 = "", "", ""  # use global variable for time being
common_subsequence = ""

#TODO onderstaand algoritme is serious toe aan een update; dit klopt nog niet.

def output_alignment(A, B, C, D, i, j, k):
    global l1, l2, l3, common_subsequence
    if i == 0 and j == 0 and k == 0:
        return
    if i > 0 and D[i][j][k] > D[i - 1][j][k]:
        output_alignment(A, B, C, D, i - 1, j, k)
        l1, l2, l3 = l1 + A[i], l2 + "-", l3 + "-"
    elif j > 0 and D[i][j][k] > D[i][j - 1][k]:
        output_alignment(A, B, C, D, i, j - 1, k)
        l1, l2, l3 = l1 + "-", l2 + B[j], l3 + "-"
    elif k > 0 and D[i][j][k] > D[i][j][k - 1]:
        output_alignment(A, B, C, D, i, j, k - 1)
        l1, l2, l3 = l1 + "-", l2 + "-", l3 + C[k]
    elif i > 0 and j > 0 and D[i][j][k] > D[i - 1][j-1][k]:
        output_alignment(A, B, C, D, i - 1, j-1, k)
        l1, l2, l3 = l1 + A[i], l2 + B[j], l3 + "-"
    elif j > 0 and k > 0 and D[i][j][k] > D[i][j-1][k-1]:
        output_alignment(A, B, C, D, i, j-1, k-1)
        l1, l2, l3 = l1 + "-", l2 + B[j], l3 + C[k]
    elif i > 0 and k > 0 and D[i][j][k] > D[i-1][j][k-1]:
        output_alignment(A, B, C, D, i-1, j, k-1)
        l1, l2, l3 = l1 + A[i], l2 + "-", l3 + C[k]

    else:
        output_alignment(A, B, C, D, i - 1, j - 1, k-1)
        l1, l2, l3 = l1 + A[i], l2 + B[j] + C[k]
        if A[i] == B[j] == C[k]:
            common_subsequence = common_subsequence + A[i]
        print(A[i], B[j], C[k])
    return l1, l2, l3, common_subsequence


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    # added 0 to the strings in order to let the index run from 0-n
    A = "0" + first_sequence
    B = "0" + second_sequence
    C = "0" + third_sequence

    n = len(A)
    m = len(B)
    p = len(C)

    # Q = np.array(n,m,p)

    D = [[[0 for _ in range(p)] for _ in range(m)] for _ in range(n)]  # create a mxnxp list

    for i in range(n):
        D[i][0][0] = i
    for j in range(m):
        D[0][j][0] = j
    for k in range(p):
        D[0][0][k] = k
    for k in range(1, p):
        for j in range(1, m):
            for i in range(1, n):
                if B[j] == C[k]:
                    insertion1 = D[i][j - 1][k - 1] + 1
                else:
                    insertion1 = D[i][j - 1][k - 1] + 2

                if A[i] == C[k]:
                    insertion2 = D[i - 1][j][k - 1] + 1
                else:
                    insertion2 = D[i - 1][j][k - 1] + 2

                if A[i] == B[j]:
                    insertion3 = D[i - 1][j - 1][k] + 1
                else:
                    insertion3 = D[i - 1][j - 1][k] + 2
                insertion = min(insertion1, insertion2, insertion3)

                deletion12 = D[i][j][k - 1] + 2
                deletion13 = D[i][j - 1][k] + 2
                deletion23 = D[i - 1][j][k] + 2
                deletion = min(deletion12, deletion13, deletion23)

                match3 = D[i - 1][j - 1][k - 1]
                match2 = D[i - 1][j - 1][k - 1] + 1
                match2 = D[i - 1][j - 1][k - 1] + 1
                match2 = D[i - 1][j - 1][k - 1] + 1
                match0 = D[i - 1][j - 1][k - 1] + 2

                if A[i] == B[j] == C[k]:  # 3 matches
                    D[i][j][k] = min(insertion, deletion, match3)
                if A[i] != B[j] != C[k]:  # no matches
                    D[i][j][k] = min(insertion, deletion, match0)
                else:  # 2 matches
                    D[i][j][k] = min(insertion, deletion, match2)

    print("alignment: ")
    l1, l2, l3, l4 = output_alignment(A, B, C, D, n - 1, m - 1, p - 1)
    print(l1)
    print(l2)
    print(l3)
    print(l4)

    return D[n - 1][m - 1][p - 1]


if __name__ == '__main__':
    print(lcs3(input(), input(), input()))

    # n = int(input())
    # a = list(map(int, input().split()))
    # assert len(a) == n
    #
    # m = int(input())
    # b = list(map(int, input().split()))
    # assert len(b) == m
    #
    # q = int(input())
    # c = list(map(int, input().split()))
    # assert len(c) == q
    #
    # print(lcs3(a, b, c))
