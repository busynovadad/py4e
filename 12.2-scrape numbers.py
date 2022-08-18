import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = "http://www.dr-chuck.com/page1.htm"
# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_1596278.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
summed = 0
tags = soup('td')
for tag in tags:
    # print(tag.contents)
    for child in tag.descendants:
        # print(child)
        s = str(child)
        if s.isnumeric():
            print(s)
            summed = summed + int(s)
    # print(tag.get('span', None))
print(summed)



