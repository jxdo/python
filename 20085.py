# coding:gbk
__author__ = '1'
def is_repeat(numstr):
    for num in range(0, len(numstr), 1):
        if numstr.count(numstr[num]) > 1:
            return True
    return False
for a in range(10000, 79999, 1):
    b = a + 20085
    c = str(a)+str(b)
    if is_repeat(c) == False:
        print c
