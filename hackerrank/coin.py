

def solve(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
            else:
                break

    return 1 if dp[amount] > amount else dp[amount]


def solve2(coins, amount):
    count = 0
    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            count += 1

    return count


def solve3(coins, amount):
    count = 0
    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            count += 1

    return count


print(solve2([5, 2, 1], 11))
