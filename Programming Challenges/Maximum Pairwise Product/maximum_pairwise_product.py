# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    maxindex1 = 0
    for i in range(len(numbers)):
        if (numbers[i] > numbers[maxindex1] or maxindex1 == -1):
            maxindex1 = i

    maxindex2 = -1
    for i in range(len(numbers)):
        if (i != maxindex1) and ((numbers[i] > numbers[maxindex2]) or maxindex2 == -1):
            maxindex2 = i

    return numbers[maxindex1] * numbers[ maxindex2]


    # type here


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))

