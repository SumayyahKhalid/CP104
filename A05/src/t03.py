"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""
# Imports
from functions import open_triangle
# Constants

n = -1
while n < 0:
    n = int(input("Enter a positive integer number: "))
    open_triangle(n)
