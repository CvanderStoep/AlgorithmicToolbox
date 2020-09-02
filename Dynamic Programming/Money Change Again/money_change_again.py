# python3
import math

def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1, 3, 4]
    MinNumCoins = [math.inf] * (money + 1) #maxint
    MinNumCoins[0] = 0

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                numCoins = MinNumCoins[m - coin] + 1
                if numCoins < MinNumCoins[m]:
                    MinNumCoins[m] = numCoins

    return MinNumCoins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change_naive(amount))
    print(change(amount))
