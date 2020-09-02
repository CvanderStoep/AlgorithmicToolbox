# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    if money == 0:
        return 0
    if money >= 10:
        return 1 + money_change(money - 10)
    if money >= 5:
        return 1 + money_change(money - 5)
    if money >= 1:
        return 1 + money_change(money - 1)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
