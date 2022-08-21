def getlinks(p_url, p_position):
    # print('welcome to getlinks')
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # p_url =
    # url = input('Enter - ')
    print('Retrieving:', p_url)
    html = urllib.request.urlopen(p_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = 0

    tags = soup('a')
    for tag in tags:
        count += 1
        # print(count, tag.get('href', None))
        if count == p_position:
            return tag.get('href', None)


def followurls(p_count, p_position, p_url):
    # url_to_chase = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    url_to_chase = p_url
    count = int(p_count)
    position = int(p_position)
    # print('you passed me', p_count, ' // ', p_position, ' // ', p_url)
    for x in range(count+1):
        # print('starting chase at ', x)
        # print('pre: ', url_to_chase)
        url_to_chase = (getlinks(url_to_chase, position))
        # print('post: ', url_to_chase)


u = input("Enter URL:")
c = input("Enter count:")
p = input("Enter position:")
followurls(c, p, u)
# followurls("4", "3", 'http://py4e-data.dr-chuck.net/known_by_Fikret.html')

