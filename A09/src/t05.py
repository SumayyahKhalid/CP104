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


students = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_info(students)
close(students)
