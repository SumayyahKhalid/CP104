"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-11-14"
-------------------------------------------------------
"""
# Imports

# Constants


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num + 1):
        product = product * i
    return product


def calories_burned(per_minute, minutes):
    m = 0
    curr_cal = 0
    for i in range(0, minutes, 5):
        m += 5
        curr_cal += (5 * per_minute)
        print("{:>4d}{:1s}{:>7.1f}".format(m, ":", curr_cal))
    return m


def open_triangle(num_rows):
    for i in range(num_rows):
        print("#" + (" " * i) + "#")
    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("\t", end=" ")
    for i in range(start, stop + 1):
        print(i, "\t", end=" ")
    print()

    print("", end="\t")
    print('-' * (stop - start + 1) * 7)

    for i in range(start, stop + 1):
        print(i, " |", end="")
        for j in range(start, stop + 1):
            print("\t", i * j, end="")
        print()
    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += (start + i * increment)
    return total
