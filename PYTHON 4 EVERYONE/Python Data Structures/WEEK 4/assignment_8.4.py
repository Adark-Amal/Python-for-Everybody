"""
    8.4 Open the file romeo.txt and read it line by line. For each line,
    split the line into a list of words using the split() method.
    The program should build a list of words.
    For each word on each line check to see if the word is already in the list and if not append it to the list.
    When the program completes, sort and print the resulting words in alphabetical order.
    You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

file_name = input("Enter file name: ")
file = open(file_name)
my_list = []
for line in file:
    line.rstrip()
    words = line.split()                  # splits the lines into words
    for word in words:
        if word in my_list:
            continue
    my_list.append(word)                  # if word is not in the empty list, add that word to the list
    my_list.sort()                        # sort the list
print(my_list)
