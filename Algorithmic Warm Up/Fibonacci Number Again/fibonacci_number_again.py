# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    # Calculate the Pisano period (series repeats itself starting with 0, 1)
    F0 = 0
    F1 = 1
    pisano_period = 0
    while (True):
        F0, F1 = F1, (F0 + F1) % m
        # print(F0, F1)
        pisano_period += 1
        if F0 == 0 and F1 == 1:
            break

    # Fn(mod m) = Fn, mod P (mod m)
    n = n % pisano_period
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again_naive(input_n, input_m))
    print(fibonacci_number_again(input_n, input_m))
