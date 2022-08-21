import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = "http://www.dr-chuck.com/page1.htm"
url = 'http://www.cnn.com'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))




