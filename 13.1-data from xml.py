import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
summed = 0
while True:
    address = "http://py4e-data.dr-chuck.net/comments_1596280.xml"
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    tree = ET.fromstring(data)
    results = tree.findall('.//count')
    for r in results:
        count += 1
        summed = summed + int(r.text)
    break
print('Count:', count)
print('Sum:', summed)
