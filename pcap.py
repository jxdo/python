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
# ���¼���ÿ���ļ����ļ�ͷ���ȣ��ܳ��ȼ�ȥ�������ļ������ٳ���5
print "�ļ�ͷ����Ϊ��"
print (length-525701)/5

# ���¼����ļ���md5ֵ��sha1ֵ�Ƿ�͸�����ֵ���

file_str = open("C:\\Users\\1\\Desktop\\ctf_fly\\data\\out.rar", 'rb').read()
m = hashlib.md5()
m.update(file_str)
md5 = m.hexdigest()
sha1 = hashlib.sha1(file_str).hexdigest()
if md5 == "e023afa4f6579db5becda8fe7861c2d3":
    print md5
    print "MD5 ֵУ����ȷ"
    if sha1 == "ecccba7aea1d482684374b22e2e7abad2ba86749":
        print sha1
        print "SHA1 У����ȷ"
    else:
        print "SHA1 У��ʧ��"
else:
    print "MD5 У��ʧ��"

