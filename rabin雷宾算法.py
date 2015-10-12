# coding:gbk
import math
import os,sys
import hashlib
__author__ = 'Administrator'
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def bin2dec(string_num):
    return str(int(string_num, 2))

pk = 523798549  # 公钥
c_out = 162853095  # 密文
start = 100000000
end = 999999999
while start < end:
    c = (start*start) % pk
    if c == c_out:
        print dec2bin(str(start))
    start += 1  # 计算完成要立即进行比较，否则多加了一就不对了
print 'the end'

con = '10010011100100100101010'
m = hashlib.md5()
m.update(bin2dec(con))
psw = m.hexdigest()
print psw

# check = '110001'
# output = ''
# for i in range(0, len(pk)):
#     print math.sqrt(int(c[i]))

    #
    # for x in range(0, len(c_out)):
    #     mi = int(str(start)[x])
    #     ci = mi*mi % int(pk[x])
    #     c += str(ci)
    # start += 1
    # print c
#     # output += chr(math.sqrt(int(c[i])) % int(pk[i]))
# # print output