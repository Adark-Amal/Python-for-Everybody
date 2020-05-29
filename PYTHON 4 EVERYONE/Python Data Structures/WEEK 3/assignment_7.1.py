"""
    7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
    and print the contents of the file in upper case.
    Use the file words.txt to produce the output below.
"""
# ask user to enter the file name
file_name = input("Enter file name: ")

# open the file
file = open(file_name)

# read content of the file and convert to uppercase using the upper method
file_content = file.read().upper()
print(file_content)
