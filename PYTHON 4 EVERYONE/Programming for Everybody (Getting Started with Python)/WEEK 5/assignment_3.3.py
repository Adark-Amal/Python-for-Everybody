"""
    3.3 Write a program to prompt for a score between 0.0 and 1.0.
    If the score is out of range, print an error.
    If the score is between 0.0 and 1.0, print a grade using the following table:
    Score Grade
    >= 0.9 A
    >= 0.8 B
    >= 0.7 C
    >= 0.6 D
    < 0.6 F
    If the user enters a value out of range, print a suitable error message and exit.
    For the test, enter a score of 0.85.
"""

# use try and except to detect any error in the program and exit gracefully
try:
    score = float(input('Enter your score: '))   # takes score from the user and converts to float data type
except:
    print('Invalid Input, Try again')
    exit()

# Checks to see if score falls in range and prints out results accordingly
if 0.9 <= score < 1.0:
    print('A')
elif 0.8 <= score < 0.9:
    print('B')
elif 0.7 <= score < 0.8:
    print('C')
elif 0.6 <= score < 0.7:
    print('D')
elif 0.6 > score > 0.0:
    print('E')
else:
    print('Incorrect Score')
