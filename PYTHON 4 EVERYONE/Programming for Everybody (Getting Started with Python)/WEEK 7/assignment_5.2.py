"""
    5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
    Once 'done' is entered, print out the largest and smallest of the numbers.
    If the user enters anything other than a valid number catch it with a try/except
    and put out an appropriate message and ignore the number.
    Enter 7, 2, bob, 10, and 4 and match the output below.
"""

largest = None
smallest = None

while True:                      # an infinite loop to keep the program running
    user_input = input("Enter a number: ")
    if user_input == "done":
        break                   # if user input is done, the loop ends

# catch an exception when there is an error. continue allows the loop to restart without executing remaining codes.
    try:
        num = int(user_input)
    except:
        print("Invalid input. Enter a valid number or 'done'")
        continue

# checks if user input number is largest or smallest
    if smallest == None and largest == None:
        smallest = num
        largest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")
