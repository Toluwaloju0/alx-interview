#!/usr/bin/python3
"""A module to get the winner of a prime game"""


def is_prime(num):
    """To check if a nymber is a prime number
    """

    if num == 0 or num == 1:
        return True
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def isWinner(x, nums):
    """A function to play a prime game between Maria and Ben
    Maria goes first always and chooses prime numbers in a given
    range
    if no more prime number to chose the player wins
    """
    ben_score = 0
    maria_score = 0

    for num in nums:
        x -= 1
        game_score = 0
        while num > 0:
            if is_prime(num):
                game_score += 1
            num -= 1
        # if game_score is odd Ben wins else Maria wins
        if game_score % 2 == 1:
            ben_score += 1
        else:
            maria_score += 1
        if x == 0:
            break
    if ben_score > maria_score or maria_score == 0:
        return "Ben"
    return "Maria"
