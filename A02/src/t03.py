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

date = int(input("Enter a date in the format DDMMYYYY: "))
year = date % 10000
date = date // 10000
month = date % 100
day = date // 100
print(f"The reformatted date: {year:04d}/{month:02d}/{day:02d}")
