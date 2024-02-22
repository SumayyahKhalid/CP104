"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-11-11"
-------------------------------------------------------
"""
# Imports

# Constants


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    week_days = ["Sunday", "Monday", "Tuesday",
                 "Wednesday", "Thursday", "Friday", "Saturday"]
    return week_days[d - 1]


from random import randint


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    list_int = ['n', 'low', 'high']
    randint(low, high)
    list = list_int
    return list


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        if i not in source2 and i not in target:
            target.append(i)

    for i in source2:
        if i not in source1 and i not in target:
            target.append(i)

    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for i in source1:
        if i not in source2 and i not in target:
            target.append(i)

    for i in source2:
        if i not in source1 and i not in target:
            target.append(i)

    return target
