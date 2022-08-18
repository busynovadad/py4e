import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #address = input('Enter location: ')
    address = "Pontificia universidad catolica de chile"
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    # break

    try:
        js = json.loads(data)
    except:
        js = None
    print(js)

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        break
        # continue

    # print(json.dumps(js, indent=4))
    ls = js['results'][0]['place_id']
    print(ls)

    #
    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)
    break
