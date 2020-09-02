# python3
# https://www.techiedelight.com/longest-common-subsequence/#:~:text=The%20longest%20common%20subsequence%20%28LCS%29%20is%20the%20problem,the%20second%20original%20sequence%20by%20deleting%20other%20items.


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    m = len(first_sequence)
    n = len(second_sequence)

    # lookup table stores solution to already computed sub-problems
    # i.e. T[i][j] stores the length of LCS of substring
    # X[0..i-1] and Y[0..j-1]
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if first_sequence[i - 1] == second_sequence[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if current character of X and Y don't match,
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    # LCS will be last entry in the lookup table

    return T[m][n]


if __name__ == '__main__':
    # n = int(input())
    # a = list(map(int, input().split()))
    # assert len(a) == n
    #
    # m = int(input())
    # b = list(map(int, input().split()))
    # assert len(b) == m

    print(lcs2(input(), input()))
