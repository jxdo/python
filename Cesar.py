#coding:gbk
# import string

__author__ = 'Administrator'

# ------------------- �������뻹ԭ���� ����

password = 'smg qa 44P3847RQ58C'
for x in range(26):
    output = ''
    for char in password.lower():
        chartemp = ord(char) - x
        if chartemp < 97:
            chartemp += 26
        output += chr(chartemp)
    print str(x) + ': ' + output

# # -------------------����������ܹ���
# password = '44P3847RQ58C'
# shift = 13  # λ�ƣ��൱�ڿ����������Կ
# output = ''
# for char in password:
#     chartemp = ord(char)+shift  # ���ܵĹ��̾�������13λ
#     if 90 < chartemp < 97 or chartemp > 122:  # ���ݴ�Сд # ������z�󷵻ص�a
#         chartemp -= 26
#     output += chr(chartemp)
# print output



