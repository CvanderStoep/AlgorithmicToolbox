# python3
from itertools import permutations, chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def maximum_gold_permutations(capacity, weights):
    overall_maximum = 0
    for weight_set in powerset(weights):
        current_capacity = capacity
        current_maximum = 0
        for weight in weight_set:
            if current_capacity >= weight:
                current_capacity = current_capacity - weight
                current_maximum += weight
            overall_maximum = max(overall_maximum, current_maximum)
    return overall_maximum

def Knapsack(capacity, weights):
    weights = [0] + weights
    n = len(weights)
    m = capacity + 1
    value = [[0] * m for i in range(n)] #create a nxm list
    for i in range(1,n):
        for w in range(1,m):
            value[i][w] = value[i-1][w]
            if weights[i] <= w:
                val = value[i-1][w-weights[i]] + weights[i] #all v_i are w_i
                if value[i][w] < val:
                    value[i][w] = val
    return value[n-1][m-1]

def maximum_gold_greedy(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # Greedy algorithm; is not stable
    weights.sort(reverse=True)
    current_maximum = 0
    for weight in weights:
        if capacity >= weight:
            capacity = capacity - weight
            current_maximum += weight
    return current_maximum


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))

    input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold_greedy(input_capacity, input_weights))
    print(maximum_gold_permutations(input_capacity, input_weights))
    print(Knapsack(input_capacity, input_weights))
