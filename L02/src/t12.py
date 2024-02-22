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


tsec = int(input("Number of Seconds: "))
day = tsec // (86400)
tsec = tsec % (86400)
hour = tsec // 3600
tsec %= 3600
SECPERMIN = 60
Minutes = tsec // SECPERMIN
tsec %= 60
seconds = tsec
print('days: ', day, 'hours: ', hour, 'minutes: ',
      Minutes, 'seconds: ', seconds,)
