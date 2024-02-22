"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""
# Imports
from functions import file_head
# Constants


fh = open("functions.py", "r", encoding="utf-8")
file_head(fh, 5)
fh.close()
