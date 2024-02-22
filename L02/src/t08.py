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
d1 = float(input("Enter your height (m): "))
n1 = float(input("Enter your weight (kg): "))
limit = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

BMI = n1 / (d1**2)
prime = BMI / limit

print("Body Mass Index (kg/m^2)= ", BMI)
print("BMI Prime= ", prime)
