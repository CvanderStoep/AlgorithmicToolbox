# python3
import math

def Digits_and_Operators(dataset):
    #only positive single digits
    #only + - * operators
    digits = list(map(int, dataset[::2]))
    operators = list(dataset[1::2])
    return digits, operators


def doMath(operator, digit1, digit2):
    if operator == "*" or operator == "x":
        return digit1 * digit2
    elif operator == "+":
        return digit1 + digit2
    else:  # -
        return digit1 - digit2

def MinandMax(i, j, m, M, digits, operators):
    min_value = math.inf
    max_value = - math.inf
    for k in range(i,j):
        a = doMath(operators[k], M[i][k], M[k+1][j])
        b = doMath(operators[k], M[i][k], m[k+1][j])
        c = doMath(operators[k], m[i][k], M[k+1][j])
        d = doMath(operators[k], m[i][k], m[k+1][j])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def Parentheses(digits, operators):
    n = len(digits)
    M = [[0] * (n + 1) for i in range(n + 1)]  # create a (n * n list)
    m = [[0] * (n + 1) for i in range(n + 1)]  # create a (n * n list)
    digits = [0] + digits #use d1 - dn
    operators = ["?"] + operators # use op1 - opn-1
    #in the algorithm use is made of 1 t/m n (versus 0 t/m n-1)
    for i in range(1, n+1):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1,n):
        for i in range(1,n-s+1):
            j = i+s
            m[i][j], M[i][j] = MinandMax(i, j, m, M, digits, operators)

    return M[1][n]


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    digits, operators = Digits_and_Operators(dataset)

    return Parentheses(digits, operators)


if __name__ == "__main__":
    print("maximum value= ", find_maximum_value(input()))
