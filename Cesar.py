#coding:gbk
# import string

__author__ = 'Administrator'

# ------------------- 凯撒密码还原过程 左移

password = 'smg qa 44P3847RQ58C'
for x in range(26):
    output = ''
    for char in password.lower():
        chartemp = ord(char) - x
        if chartemp < 97:
            chartemp += 26
        output += chr(chartemp)
    print str(x) + ': ' + output

# # -------------------凯撒密码加密过程
# password = '44P3847RQ58C'
# shift = 13  # 位移，相当于凯撒密码的秘钥
# output = ''
# for char in password:
#     chartemp = ord(char)+shift  # 加密的过程就是右移13位
#     if 90 < chartemp < 97 or chartemp > 122:  # 根据大小写 # 当超出z后返回到a
#         chartemp -= 26
#     output += chr(chartemp)
# print output



