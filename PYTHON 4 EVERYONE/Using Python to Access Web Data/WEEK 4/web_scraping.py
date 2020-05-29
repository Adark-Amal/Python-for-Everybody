import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    number = int(tag.text)
    count += 1
    total = total + number

print(f'Count: {count}')
print(f'Sum: {total}')