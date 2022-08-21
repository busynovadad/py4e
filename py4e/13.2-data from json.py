import urllib.request
# import urllib.parse
import urllib.error
# import xml.etree.ElementTree as ET
import ssl
import json
import requests

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
summed = 0

# address = "http://py4e-data.dr-chuck.net/comments_42.json"
address = "http://py4e-data.dr-chuck.net/comments_1596281.json"
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(data)

info = json.loads(data)
print('User count:', len(info))
# info is a dict
# print(type(info))
countSum = 0
for item in info["comments"]:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
#     if item == "comments":
#         print('foo')
#         for pcs in item:
#             print(pcs)

    print(item['name'])
    print(item['count'])
    countSum += item['count']

# r = requests.get(url)
# rd = r.json()
# entries = rd["comments"]["count"]
# print(entries)

print(countSum)
