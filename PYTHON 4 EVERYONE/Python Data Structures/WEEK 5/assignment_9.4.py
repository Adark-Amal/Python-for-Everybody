"""
    9.4 Write a program to read through the mbox-short.txt
        and figure out who has sent the greatest number of mail messages.
        The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
        The program creates a Python dictionary that maps the sender's mail address
        to a count of the number of times they appear in the file. After the dictionary is produced,
        the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

inp = input("Enter file: ")
my_file = open(inp)
my_dict = dict()                # create empty dictionary using dict constructor

for line in my_file:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    for word in words:
        word = words[1]
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] = my_dict[word] + 1

        # or use the get method i.e my_dict[word] = my_dict.get(word, 0) + 1

print(my_dict)

my_email = None
email_count = None
for key, val in list(my_dict.items()):             # my_dict.items() creates a list of tuples with both key and value
    if email_count == None or val > email_count:   # checks for most prolific committer
        my_email = key
        email_count = val

print(my_email, email_count)                       # print the email and count of the most prolific committer


