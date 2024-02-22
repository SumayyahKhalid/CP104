"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""

p = float(input("Principal: $"))
r = float(input("Interest (decimal): "))
t = int(input("Number of years: "))
n = int(input("Number of times interest compounded per year: "))

d = r / n
e = n * t

money = p * (1 + d) ** e

print(f"Balance: $ {money}")
