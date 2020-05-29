"""
    3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
   Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
   Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
   You should use input to read a string and float() to convert the string to a number.
   Do not worry about error checking the user input - assume the user types numbers properly.
"""

# Ask the user input which is usually a string and convert the input to float data type
user_input1 = input("Enter number of hours: ")
hours = float(user_input1)

# Ask for user input which is usually a string and convert the input to float data type
user_input2 = input("Enter rate: ")
rate = float(user_input2)

# Check if user worked beyond 40 hours and compute grosspay accordingly
if hours > 40:
    grossPay = (40 * rate) + (rate * 1.5) * (hours - 40)
else:
    grossPay = hours * rate

print("Pay:", grossPay)
