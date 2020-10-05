# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    lastwin = 1
    while (lastwin <= n):
        n = n - lastwin
        summands.append(lastwin)
        lastwin += 1

    summands[-1] = summands[-1] + n


    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
