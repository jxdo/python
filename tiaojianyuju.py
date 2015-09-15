# coding:gbk
__author__ = 'Administrator'
'''
while True:
    word = raw_input('please input a word ')
    if word == 'breakout':
        break
    print 'the word is ' + word
'''
# ----------------------while\for循环中的else语句仅在未调用break时执行。
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
    elif root == 4:
        pass      # 此处的条件语句中没有内容，在python中是非法的可用pass跳过

else:
    print 'no find it'
# ----------------列表推导式-轻量级循环
print [x*x for x in range(10)]  # x的内容为后面循环中的内容
print [x*y for x in range(10) for y in range(5)]
# ------------------pass del  exec
x = [1, 2, 3, 4, 5]
y = x
y[1] = 10
print x      # y=x 以后y和x指向了同一个值，并没有完全复制过来，因此y改变后x也会改变
del x        # 虽然x、y指向同一个值，使用del只是删除了名称，并没有删除值
print y
# ------------------exec eval 动态创建python代码  谨慎使用
exec "print 'hello word'" # 执行python语句
eval(raw_input("input an expression;"))  # 执行python表达式