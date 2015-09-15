# coding:gbk
import hashlib
__author__ = 'Administrator'
# ----------------------判断是否为素数
def issushu(num):
    if num <= 1:
        return False
    x = 2
    while x*x < num:
        if num % x == 0:
            return True
        x += 1
        return False
# ----------------------
num = 98554799767
x = 2
big = 0
small = 0
while x*x < num:
    if num % x == 0:
        num1 = num/x
        if issushu(num1) == False:
            if num1 > x:
                big = num1
                small = x
            else:
                big = x
                small = num1
    x += 1
output = str(small)+str(big)
m = hashlib.md5()
m.update(output)
psw = m.hexdigest()
print psw