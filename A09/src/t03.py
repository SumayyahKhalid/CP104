"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import file_stats
# Constants

dfh = open("functions.py", "r", encoding="utf-8")
ucount, lcount, dcount, wcount = file_stats(fh)
close(fh)
