"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""
pr = int(input("Mortgage principal ($): "))
num = int(input("Number of years: "))
rate = float(input("Yearly interest rate (%): "))

n2 = num * 12
i2 = rate / 100 / 12
numerator = i2 * (1 + i2)**n2
denominator = ((1 + i2)**n2) - 1
mo = pr * (numerator / denominator)


print("The monthly payments are: ", mo)
