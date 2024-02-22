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


def winner():
    """
    -------------------------------------------------------
    Winner takes no parameters and asks the user to enter a 
    series of strings that represent the output of a game with a loop. 
    Use: winner()
    -------------------------------------------------------
    Parameters:
        blue, grey
    Returns:
        blue, grey
    ------------------------------------------------------
    """
    blue = 0
    grey = 0
    while True:
        team = input("Enter the winning team: ")
        if team == '':
            break
        if team == "blue":
            blue += 1
        if team == "grey":
            grey += 1
    return blue, grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if (num == 1):
        return False

    x = 2
    while x < num:

        if num % x == 0:
            return False
        x += 1

    return True


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    if principal <= 0:
        raise ValueError("Principal should be>0")
    if rate < 0:
        raise ValueError("Rate should be>=0")
    if payment < 0:
        raise ValueError("Payment should be>0")

    print('interest_table(', principal, ', ', str(
        rate * 100), ', ', str(payment), ')', sep='')
    print(f"Principal : ${principal:.2f}")
    print(f"Interest rate : {rate:.2f} %")
    print(f"Monthly payment : ${payment:.2f}")
    print("------------------------------------")
    print(f"""{'Month':>5s}""", end=' ')
    print(f"""{'Interest':>9s}""", end=' ')
    print(f"""{'Payment':>9s}""", end=' ')
    print(f"""{'Balance':>9s}""", end=' ')
    print("------------------------------------")

    month = 1
    balance = principal
    while(balance > 0):
        print(f"{month:5d}", end=' ')
        # Calculate interest for current month
        interest = balance * rate / 1200
        print(f"{interest:9.2f}", end=' ')
        # Add interest to current due
        balance += interest
        # Check if balance is more than the monthly payment
        if balance < 100:
            payment = balance
        print(f"{payment:9.2f}", end=' ')
        # Reduce balance by payment
        balance -= payment
        print(f"{balance:9.2f}")
        month += 1

    return month


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    if num == 0:
        return 1
    count = 0
    if num < 0:
        num *= -1
    while num > 0:
        num //= 10
        count += 1
    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i += 1
    return total
