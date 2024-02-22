"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""
# Imports
import random
import string
# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    count = 0
    matrix = []
    if(value_type == "float"):
        for x in range(rows):
            matrix.append([])
            for y in range(cols):
                matrix[count].append(random.uniform(low, high))
            count += 1
    if(value_type == "int"):
        for x in range(rows):
            matrix.append([])
            for y in range(cols):
                matrix[count].append(random.randint(low, high))
            count += 1
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    count = 0
    letters = string.ascii_lowercase
    matrix = []
    for x in range(rows):
        matrix.append([])
        for y in range(cols):
            matrix[count].append(random.choice(letters))
        count += 1
    return matrix


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            num = matrix[x][y]
            if(num < smallest):
                smallest = num
            if(num > largest):
                largest = num
            total += num
            count += 1
    average = total / count
    return smallest, largest, total, average


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            num1 = matrix[x][y]
            matrix[x][y] = num1 * num
    return


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = True
    if(len(matrix1[0]) == len(matrix2[0]) and len(matrix1) == len(matrix2)):
        i = 0
        n = len(matrix1[0])
        m = len(matrix1)
        while(i < m):
            j = 0
            while(j < n):
                if(matrix1[i][j] != matrix2[i][j]):
                    equal = False
                    break
                j += 1
            if(equal == False):
                break
            i += 1
    else:
        equal = False
    return equal
