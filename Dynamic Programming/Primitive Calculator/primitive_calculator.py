# python3
import math

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    OperSeq = {"1": [1]} # make a dictionary value, list

    for m in range(2, n + 1):
        MinSeq = OperSeq[str(m-1)].copy() #operator is: +1
        MinLength = len(MinSeq)
        if m%2 == 0: #operator is: *2
            LenSeq = len(OperSeq[str(m//2)])
            if LenSeq < MinLength:
                MinSeq = OperSeq[str(m//2)].copy()
        if m%3 == 0: #operator is: *3
            LenSeq = len(OperSeq[str(m//3)])
            if LenSeq < MinLength:
                MinSeq = OperSeq[str(m//3)].copy()
        MinSeq.append(m)
        OperSeq[str(m)] = MinSeq#.copy()

    return OperSeq[str(m)]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
