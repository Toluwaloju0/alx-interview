#!/usr/bin/python3
"""A module to create the making change"""


def makeChange(coins, total):
    """A function to implement the making change algorithm"""

    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1

    given_coin = 0
    coins.sort(reverse=True)
    while total > 0:
        if total < coins[-1]:
            return -1
        # iterate through the coins to find the
        # highest coin in respect to total
        for coin in coins:
            if total >= coin:
                total = total - coin
                given_coin += 1
                break
    return given_coin
