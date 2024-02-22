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


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    fh.seek(0)
    i = 0
    line = fh.readline()
    while line != "" and i < linecount:
        print(line.strip())
        i = i + 1
        line = fh.readline()
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    lst = []
    line = fh.readline()

    for i in numbers:
        if i > 0:
            numbers = line.strip().split(',')
            lst = lst.append(numbers)
        return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount, lcount, dcount, wcount = 0, 0, 0, 0
    # loop for each line
    for lines in fh:
        # loop for each character in lines
        for char in lines:
            # if character is uppercase letter
            if ord(char) >= ord('A') and ord(char) <= ord('Z'):
                ucount += 1
            # if character is lowercase letter
            elif ord(char) >= ord('a') and ord(char) <= ord('z'):
                lcount += 1
            # if character is digit
            elif char.isnumeric():
                dcount += 1
            # if character is whitespace
            elif char == ' ':
                wcount += 1
    # return the all count
    return ucount, lcount, dcount, wcount


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    i = 0
    for line in fh_in:
        line = "[{}] {}".format(i, line.strip())
        print(line, file=fh_out)
        i = i + 1
    return


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    SURNAME = 0
    FORENAME = 1
    ID = 2
    MARK = 3

    students.seek(0)
    student = students.readline()
    data = student.split(",")
    mark = int(data[MARK])
    avg = mark
    total = mark
    lowest = mark
    highest = mark
    l_id = data[ID]
    h_id = data[ID]
    n = 1
    for student in students:
        data = student.split(",")
        mark = int(data[MARK])
        total += mark
        n += 1
        if mark < lowest:
            lowest = mark
            l_id = data[ID]
        elif mark > highest:
            highest = mark
            h_id = data[ID]
        avg = total / n

    return l_id, h_id, avg
