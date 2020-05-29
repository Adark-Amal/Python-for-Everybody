import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter your url: ")
data = urllib.request.urlopen(url).read()

info = json.loads(data)

print(f'Retrieving {url}')

count = 0
total = 0
for item in info['comments']:
    count += 1
    total += item['count']

print (f'Total: {total}')
print (f'Count: {count}')