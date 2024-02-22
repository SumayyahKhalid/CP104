"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports

# Constants


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    ans = ""
    start = 0
    end = 0
    for char in string:
        if (char >= 'A') & (char <= "Z"):
            temp = string[start:end]
            if ans != '':
                ans += ' ' + temp.lower()
            else:
                ans += temp
            start = end
        end += 1
    if ans != '':
        ans += ' ' + string[start:end].lower()
    else:
        ans += string

    return ans


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    if string.endswith('s') or string.endswith('sh') or string.endswith('ch'):
        string += 'es'
    elif string.endswith('y') and not (string.endswith('ay') or string.endswith('oy')):
        string += 'ies'
    else:
        string += 's'
    return string


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    result = ""
    i = 1
    while string2.endswith(string1[-i:]):
        result = string1[-i:]
        i += 1
    return result


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(isbn) != 17:
        return False
    for ch in isbn:
        if ch not in '0123456789-':
            return False
    groups = isbn.split('-')
    if (len(groups)) != 5:
        return False
    for group in groups:
        if len(group) == 0:
            return False
    if groups[0] != '978' and groups[0] != '978':
        return False
    if len(groups[4]) != 1:
        return False

    return True


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    ret = False
    for i, k in zip(word_list[0::2], word_list[1::2]):
        if(i[len(i) - 1] == k[0]):
            ret = True
        else:
            ret = True
    return ret
