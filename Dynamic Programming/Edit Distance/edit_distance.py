# python3

def output_alignment(A, B, D, l1, l2, common_sub, i, j):
    if i == 0 and j == 0:
        return l1, l2, common_sub
    if i > 0 and D[i][j] == D[i-1][j] + 1:
        (l1, l2, common_sub) = output_alignment(A, B, D, l1, l2, common_sub, i-1, j)
        l1, l2 = l1 + A[i], l2 + "-"
    elif j > 0 and D[i][j] == D[i][j-1] + 1:
        (l1, l2, common_sub) = output_alignment(A, B, D, l1, l2, common_sub, i, j-1)
        l1, l2 = l1 + "-", l2 + B[j]
    else:
        (l1, l2, common_sub) = output_alignment(A, B, D, l1, l2, common_sub, i-1, j-1)
        l1, l2 = l1 + A[i], l2 + B[j]
        if A[i] == B[j]:
            common_sub = common_sub + A[i]
    return l1, l2, common_sub


def edit_distance(first_string, second_string):
    # added 0 to the strings in order to let the index run from 0-n
    A = "0"+ first_string
    B = "0"+ second_string
    n = len(A)
    m = len(B)
    D = [[0] * m for i in range(n)] #create a mxn list
    for i in range(n):
        D[i][0] = i
    for j in range(m):
        D[0][j] = j
    for j in range(1,m):
        for i in range(1,n):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if A[i] == B[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    l1, l2, l3 = output_alignment(A, B, D, "", "", "", n-1, m-1)

    return D[n-1][m-1], l1, l2, l3


if __name__ == "__main__":

    print(edit_distance(input("Enter the first string: "), input("Enter the second string: ")))

