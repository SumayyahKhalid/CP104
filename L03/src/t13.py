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

tsec1 = int(input("Enter number of seconds: "))
tsec = tsec1 % (86400)
hour = tsec // 3600
tsec %= 3600
SECPERMIN = 60
Minutes = tsec // SECPERMIN
tsec %= 60
seconds = tsec
print(
    f'There are {hour} hours, {Minutes} minutes, and {seconds} seconds in {tsec1} seconds.')
