"""
    2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
    Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
    You should use input to read a string and float() to convert the string to a number.
    Do not worry about error checking or bad user data.
"""

# Ask the user input which is usually a string and convert the input to float data type
user_input1 = input("Enter number of hours: ")
hours = float(user_input1)

# Ask for user input which is usually a string and convert the input to float data type
user_input2 = input("Enter rate: ")
rate = float(user_input2)

# Compute the grosspay and print the results
grossPay = hours * rate
print("Pay:", grossPay)