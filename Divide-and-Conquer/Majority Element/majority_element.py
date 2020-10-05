# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 7
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return [e, elements.count(e)]

    return [0, 0]


def majority_element(elements):
    assert len(elements) <= 10 ** 7

    # Calls the actual routine MN
    return Majority_Number(elements, 0, len(elements) - 1)



def Majority_Number(A, low, high):
    # Maximum number, divide-and-conquer
    if low == high:
        return [A[low], 1]
    else:
        mid = low + (high - low) // 2
        m_left, c_left = Majority_Number(A, low, mid)
        m_right, c_right = Majority_Number(A, mid + 1, high)

        A_left = A[low: mid + 1]
        A_right = A[mid + 1: high + 1]

        # combine the results of the two recursive calls
        if c_left + A_right.count(m_left) > (len(A_left) + len(A_right)) / 2:
            return [m_left, c_left + A_right.count(m_left)]
        else:
            if c_right + A_left.count(m_right) > (len(A_left) + len(A_right)) / 2:
                return [m_right, c_right + A_left.count(m_right)]
            else:
                return [0, 0]


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
    print(majority_element(input_elements))
