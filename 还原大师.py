# coding:gbk
import hashlib
__author__ = 'Administrator'

char_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for char1 in char_list:
    for char2 in char_list:
        for char3 in char_list:
            output = 'TASC'+char1+'O3RJMV'+char2+'WDJKX'+char3+'ZM'
            m = hashlib.md5()
            m.update(output)
            psw = m.hexdigest()
            if 'e903' in psw:
                print output+"|zhiwei:"+psw
