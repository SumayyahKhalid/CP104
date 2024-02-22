"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Constants

digit = int(input("Enter a positive digit number: "))

answer1 = digit // 10
answer2 = digit % 10
product = answer1 * answer2

print(f"The product of the digits of {digit} is {product}")
