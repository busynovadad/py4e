search_string = 'this continent'
count = 0
try:
    xfile = open('/home/brad/testfile.txt')
    file_body = xfile.read()
    print('file body len', len(file_body))
    print(file_body[:33])
    xfile.seek(0)
    for line_in in xfile:
        # if line_in.startswith(search_string):
        #     print(line_in.replace('\n', 'zzzzzzz'))
        # print(line_in.replace('\n', ''))
        count += 1
        print(line_in.strip())
    xfile.close()
    print('count: ', count)
except:
    print('File error.')
    quit()
