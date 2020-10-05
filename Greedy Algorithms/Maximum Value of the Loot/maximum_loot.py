# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    n = len(weights)
    A = n * [0]
    V = 0
    for _ in range(n):
        if capacity == 0:
            return V
        vw_max = 0
        imax = -1
        for i in range(n):
            if weights[i] > 0 and prices[i]/weights[i] > vw_max:
                imax = i
                vw_max = prices[i]/weights[i]
        asmall = min(weights[imax], capacity)
        V = V + asmall * prices[imax] / weights[imax]
        weights[imax] = weights[imax] - asmall
        A[imax] = A[imax] + asmall
        capacity = capacity - asmall

    return V


if __name__ == "__main__":
    # data = list(map(int, stdin.read().split()))
    data = list(map(int, input().split()))

    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
