# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    if n<=1 :
        return n
    a = 0
    b = 1
    for i in range(0,n-1):
        a, b = b, (a + b) % 10

    return b


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number_naive(input_n))
    print(last_digit_of_fibonacci_number(input_n))
