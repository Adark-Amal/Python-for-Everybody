"""
2.2 Write a program that uses input to prompt a user for their name and then welcomes them.
    Note that input will pop up a dialog box.
    Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
"""

name = input("Enter your name: ")      # This statement takes the input from a user and stores in the variable name.
print("Hello", name)

# another way to output string by concatenation

print("Hello " + name)

# another way to output string by string formatting

print(f"Hello {name}")
