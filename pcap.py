# coding:gbk
import hashlib
# {"path":"fly.rar","appid":"","size":525701,"md5":"e023afa4f6579db5becda8fe7861c2d3","sha":"ecccba7aea1d482684374b22e2e7abad2ba86749","sha3":""}

f = open('C:\\Users\\1\\Desktop\\ctf_fly\\data\\out.rar', 'wb')
length = 0
for i in range(1, 6):
    print i
    path = 'C:\\Users\\1\\Desktop\\ctf_fly\\data\\'+str(i)+'.txt'
    print path
    file_object = open(path, 'rb')
    all_the_text = file_object.read()
    length += len(all_the_text)
    f.write(all_the_text[364:])
    file_object.close()
f.close()
# 以下计算每个文件的文件头长度，总长度减去给出的文件长度再除以5
print "文件头长度为："
print (length-525701)/5

# 以下计算文件的md5值和sha1值是否和给定的值相等

file_str = open("C:\\Users\\1\\Desktop\\ctf_fly\\data\\out.rar", 'rb').read()
m = hashlib.md5()
m.update(file_str)
md5 = m.hexdigest()
sha1 = hashlib.sha1(file_str).hexdigest()
if md5 == "e023afa4f6579db5becda8fe7861c2d3":
    print md5
    print "MD5 值校验正确"
    if sha1 == "ecccba7aea1d482684374b22e2e7abad2ba86749":
        print sha1
        print "SHA1 校验正确"
    else:
        print "SHA1 校验失败"
else:
    print "MD5 校验失败"

