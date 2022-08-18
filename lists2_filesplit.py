from sys import *
search_string = 'this continent'
count = 0
try:
    xfile = open('/home/brad/testfile.txt')
    file_body = xfile.read()
    # print('file body len', len(file_body))
    # print(file_body[:33])
    xfile.seek(0)
    for line_in in xfile:
        # if line_in.startswith(search_string):
        #     print(line_in.replace('\n', 'zzzzzzz'))
        # print(line_in.replace('\n', ''))
        count += 1
        print(line_in.strip())
    file_words = file_body.split()
    print(file_words[:33])
    print('file words:', len(file_words))
    xfile.close()
    print('count: ', count)
except:
    print(exc_info())
    # print('File error.')
    quit()
