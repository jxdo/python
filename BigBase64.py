import  base64
__author__ = '1'

file_object = open('C:\\Users\\1\\Downloads\\flag.txt')
try:
    all_the_text = file_object.read()
    a = base64.b64decode(all_the_text)
    f = open('C:\\Users\\1\\Downloads\\out.jpg', 'wb')
    print >> f, a
    f.close()
finally:
    file_object.close()
