# coding:gbk
__author__ = 'Administrator'
'''
while True:
    word = raw_input('please input a word ')
    if word == 'breakout':
        break
    print 'the word is ' + word
'''
# ----------------------while\forѭ���е�else������δ����breakʱִ�С�
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
    elif root == 4:
        pass      # �˴������������û�����ݣ���python���ǷǷ��Ŀ���pass����

else:
    print 'no find it'
# ----------------�б��Ƶ�ʽ-������ѭ��
print [x*x for x in range(10)]  # x������Ϊ����ѭ���е�����
print [x*y for x in range(10) for y in range(5)]
# ------------------pass del  exec
x = [1, 2, 3, 4, 5]
y = x
y[1] = 10
print x      # y=x �Ժ�y��xָ����ͬһ��ֵ����û����ȫ���ƹ��������y�ı��xҲ��ı�
del x        # ��Ȼx��yָ��ͬһ��ֵ��ʹ��delֻ��ɾ�������ƣ���û��ɾ��ֵ
print y
# ------------------exec eval ��̬����python����  ����ʹ��
exec "print 'hello word'" # ִ��python���
eval(raw_input("input an expression;"))  # ִ��python���ʽ