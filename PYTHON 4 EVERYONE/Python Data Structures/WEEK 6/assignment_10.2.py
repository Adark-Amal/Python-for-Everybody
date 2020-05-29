"""
    10.2 Write a program to read through the mbox-short.txt and
    figure out the distribution by hour of the day for each of the messages.
    You can pull the hour out from the 'From ' line by finding the time and
    then splitting the string a second time using a colon.

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

file_name = input('Enter file name: ')

try:
    my_file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

hour_time = dict()
for line in my_file:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')                  # split the extracted time by the colon delimiter
        hour = time[0]
        hour_time[hour] = hour_time.get(hour, 0) + 1    # add extracted hour to the dictionary

# dictionaries are converted to list of tuples in order to sort the elements

hourslist = []
for hour, count in hour_time.items():
    hourslist.append((hour, count))

hourslist.sort()

for hour, count in hourslist:
    print(hour, count)
