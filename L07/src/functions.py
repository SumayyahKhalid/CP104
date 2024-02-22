"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    n = randint(1, high + 1)
    count = 0
    while True:
        guess = int(input("Guess: "))
        count = count + 1
        if guess > n:
            print("Too high, try again.")
        elif guess < n:
            print("Too low, try again.")
        else:
            print("Congratulations - good guess!")
            print(f"You made {count} guesses")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    while power < target:
        power = 2 * power
    return power


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    while current < target:
        current = current + (current * (rate / 100))
        years = years + 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    minimum = None
    maximum = None
    total = 0
    count = 0
    print("First positive value: ", end="")
    num = float(input())
    if num < 0:
        return None
    minimum = num
    maximum = num
    total += num
    count += 1
    while True:
        print("Next positive value: ", end="")
        num = float(input())
        if num < 0:
            break
        if minimum > num:
            minimum = num
        if maximum < num:
            maximum = num
        total += num
        count += 1
    average = total / count
    return minimum, maximum, total, average


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
