import myxml.etree.ElementTree as ET     # my import statement wasn't working so i changed the name of the module
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a url: ")
uh = urllib.request.urlopen(url)
data = uh.read()
print(f"Retrieving {url}")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

count = 0
total = 0
for item in results:
    x = int(item.find('count').text)
    count += 1
    total = total + x

print(f'Count: {count}')
print(f'Sum : {total}')
