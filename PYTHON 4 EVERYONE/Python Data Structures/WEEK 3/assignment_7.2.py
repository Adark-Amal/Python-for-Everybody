"""
    7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
    looking for lines of the form: X-DSPAM-Confidence: 0.8475
    Count these lines and extract the floating point values from each of the lines
    and compute the average of those values and produce an output as shown below.
    Do not use the sum() function or a variable named sum in your solution.
    You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
    when you are testing below enter mbox-short.txt as the file name.
"""
# ask user for file name
file_name = input("Enter file name: ")

# open the file
file = open(file_name)

# set an initial value for count and total
count = 0
total = 0

# loop through file using the for loop
for line in file:
    line = line.rstrip()                                # strip the file of all whitespaces to the right of text
    if not line.startswith("X-DSPAM-Confidence:"):      # skip all lines not starting with X-DSPAM.....
        continue
    first_pos = line.find(":")                          # find position of a string character
    number = line[first_pos+2:]                         # use string slicing to extract string
    count += 1                                          # increment count
    total = total + float(number)                       # convert extracted number to float and add to total

print("Average spam confidence:", total/count)
