"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-09-30"
-------------------------------------------------------
"""

sweat = float(input("Enter sweatband cost: $"))
pants = float(input("Enter pants cost: $"))
jacket = float(input("Enter jacket cost: $"))

Total = sweat + pants + jacket


print(f"Clothes      Cost")
print(f"Sweatband    ${sweat:6.2f}")
print(f"Pants        ${pants:6.2f}")
print(f"Jacket       ${jacket:6.2f}")
print(f"Total        ${Total:6.2f}")
