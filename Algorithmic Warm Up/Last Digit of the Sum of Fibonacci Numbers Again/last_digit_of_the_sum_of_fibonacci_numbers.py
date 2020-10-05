# python3

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


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return (fibonacci_number_again(n + 2, 10) -1) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
    print(last_digit_of_the_sum_of_fibonacci_numbers_naive(input_n))
