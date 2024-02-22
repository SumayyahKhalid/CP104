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

# Constants


fh_in = open("wilde.txt", "r", encoding="utf-8")
fh_out = open("wilde_numbered.txt", "w", encoding="utf-8")
number_lines(fh_in, fh_out)
close(fh_in)
close(fh_out)
