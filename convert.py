# coding:gbk
import os
import os,sys
import hashlib
__author__ = 'Administrator'


# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

# bin2dec
# ������ to ʮ����: int(str,n=10)
def bin2dec(string_num):
    return str(int(string_num, 2))

# hex2dec
# ʮ������ to ʮ����
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))

# dec2bin
# ʮ���� to ������: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

# dec2hex
# ʮ���� to �˽���: oct()
# ʮ���� to ʮ������: hex()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

# hex2tobin
# ʮ������ to ������: bin(int(str,16))
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))

# bin2hex
# ������ to ʮ������: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))
#
# con = ['115739002', '214318437', '309480114', '408059549', '639537551', '738116986', '833278663', '931858098']
# for stri in con:
#     print dec2bin(stri)
con = '10010011100100100101010'
m = hashlib.md5()
m.update(bin2dec(con))
psw = m.hexdigest()
print psw