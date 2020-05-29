import re

file_name = input('Enter File name: ')

try:
    my_file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

total = 0
count = 0
for line in my_file:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    for value in number:
        if len(value) > 0:
            count = count + 1
            total = total + int(number[0])

print(f'There are {count} values with a sum = {total}')
