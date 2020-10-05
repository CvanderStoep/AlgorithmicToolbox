# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = list(map(int, numbers))
    answer = ""
    while len(numbers) != 0:
        maxdigit = numbers[0]
        for number in numbers:
            # if number >= maxdigit:
            if isgreaterorequal(number, maxdigit):
                maxdigit = number
        answer = answer + str(maxdigit) #append to string
        numbers.remove(maxdigit)
    return int(answer)

def isgreaterorequal(a,b):
    a = str(a)
    b = str(b)
    ab = int("".join([a,b]))
    ba = int("".join([b,a]))
    if ab >= ba:
        return True
    else:
        return False




if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
    print(largest_number_naive(input_numbers))
