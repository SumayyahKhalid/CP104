"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2023-01-26"
-------------------------------------------------------
"""
# Imports

# Constants


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(2, num + 1, 2):
        total = total + i
    return total


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(1, num + 1, 2):
        total = total + i
    return total


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, finish + 1, increment):
        total = total + i
    return total


def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(1, n + 1):
        total = total + 1 / i
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(height):
        for j in range(width):
            print(char, end='')
        print()
    return


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    character = 1
    spaces = (height - 1)
    for i in range(height):
        print(spaces * ' ', end='')
        spaces = spaces - 1
        print(char * character)
        character = character + 2
    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, width + 1):
        print(char * i)
        print(end='')
    for j in range(i - 1, -1, -1):
        print(char * j)
        print(end='')
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    total = 0
    for i in range(n, 0, -1):
        total = i - 1
        print(f"""
        {i} bottles of beer on the wall, {i} bottles of beer. 
        Take one down, pass it around, {total} bottles of beer on the wall.""")
        print()
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start, end + 1, inc):
        n = burnt_per_minute * i
        print(f"Calories burned after {i} minutes: {n}")
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"""Age         Salary
------------------""")
    for i in range(age, 66):
        print(f"{i:2d}{salary:15,.2f}")
        salary = (salary * (increase / 100)) + salary
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("""Year       Value $
------------------""")
    for i in range(years + 1):
        final_value = (f"{i:3d}{value:16,.2f}")
        print(final_value)
        if i < years:
            value = (value * (rate / 100)) + value
    return value


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print("""
              Cross-Sectional  Moment of  Section
Base  Height  Area             Inertia    Modulus
-------------------------------------------------""")
    for b in range(b_min, b_max + 1, b_inc):
        for h in range(h_min, h_max + 1, h_inc):
            cross_sectional_area = b * h
            moment_of_inertia = b * h**3 / 12
            section_modulus = b * h**2 / 6
            print(
                f"{b:<8} x {h:<8} {cross_sectional_area:<15.2f} {moment_of_inertia:<12.2f} {section_modulus:<8.2f}")
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    minimum = None
    maximum = None
    total = 0
    count = 0
    for i in range(n):
        print("Next value: ", end="")
        num = float(input())
        if minimum is None:
            minimum = num
            maximum = num
        else:
            if minimum > num:
                minimum = num
            if maximum < num:
                maximum = num
        total += num
        count += 1
    average = total / count
    return minimum, maximum, total, average


print(statistics(5))
