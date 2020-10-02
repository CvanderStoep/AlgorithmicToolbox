# python3

from itertools import product
from sys import stdin


def Knapsack(capacity, weights):
    weights = [0] + weights
    n = len(weights)
    m = capacity + 1
    value = [[0] * m for i in range(n)]  # create a nxm list
    for i in range(1, n):
        for w in range(1, m):
            value[i][w] = value[i - 1][w]
            if weights[i] <= w:
                val = value[i - 1][w - weights[i]] + weights[i]  # all v_i are w_i
                if value[i][w] < val:
                    value[i][w] = val
    return value[n - 1][m - 1]


def partition2(values):
    # https://en.wikipedia.org/wiki/Partition_problem
    n = len(values)
    K = sum(values)
    values = [0] + values
    if K % 2 != 0:
        return False
    K2 = int(K / 2)
    P = [[0] * (n + 1) for i in range(K2 + 1)]  # create a (K2 * (n+1) list

    for i in range(K2 + 1):
        P[i][0] = False  # first column on false
    for j in range(n + 1):
        P[0][j] = True  # top row on true

    for i in range(1, K2 + 1):
        for j in range(1, n + 1):
            index = int(i - values[j])
            if (index) >= 0:
                P[i][j] = P[i][j - 1] or P[index][j - 1]
            else:
                P[i][j] = P[i][j - 1]
    return P[K2][n]


def partition3(values):
    assert 1 <= len(values) <= 20
    # assert all(1 <= v <= 30 for v in values)
    n = len(values)
    K = sum(values)
    values = [0] + values
    if K % 3 != 0:
        return False
    K3 = int(K / 3)

    P = [[[0 for _ in range(n + 1)] for _ in range(K3 + 1)] for _ in range(K3 + 1)]  # create a (K3 * K3 * (n+1) list

    # P[i][j][k]
    # i = 0 t/m K3, sum i
    # j = 0 t/m K3, sum j
    # k = 0 t/m n, subset v1 t/m vn
    # P[i][j][k] is True:
    #     when two disjoint subsets of (v1, ..., vk)
    #     one adds up to i and the other adds up to j

    for i in range(K3 + 1):
        for j in range(K3 + 1):
            P[i][j][0] = False  # with an empty set False
    for k in range(n + 1):
        P[0][0][k] = True  # top row on true

    for j in range(1, K3 + 1):
        for k in range(1, n + 1):
            if Knapsack(j, values[1:k + 1]) == j:
                P[0][j][k] = True
            else:
                P[0][j][k] = False

    for i in range(1, K3 + 1):
        for k in range(1, n + 1):
            if Knapsack(i, values[1:k + 1]) == i:
                P[i][0][k] = True
            else:
                P[i][0][k] = False

    for i in range(1, K3 + 1):
        for j in range(1, K3 + 1):
            for k in range(1, n + 1):
                if P[i][j][k - 1]:
                    P[i][j][k] = True
                elif (j - values[k] >= 0) and P[i][j - values[k]][k - 1]:
                    P[i][j][k] = True
                elif (i - values[k] >= 0 and P[i - values[k]][j][k - 1]):
                    P[i][j][k] = True
                else:
                    P[i][j][k] = False

    return P[K3][K3][n]


def bruteforcepartition3(items):
    for partition in product([0, 1, 2], repeat=len(items)):
        sums = [sum([items[i] if partition[i] == j else 0 for i in range(len(items))]) for j in [0, 1, 2]]
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return partition


if __name__ == '__main__':
    input_n, *input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print("partition2 = ", partition2(input_values))
    print("partition3 = ", partition3(input_values))
    print("partition3 = ", bruteforcepartition3(input_values))
