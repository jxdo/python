# coding:gbk
__author__ = 'Administrator'
# ----------------------------------------------字典，字典是无序的
# 创建字典
ems = {'name': 'jxdo', 'age': '22'}
print ems
ems1 = [('name', 'df'), ('ege', '21')]
d2 = dict(ems1)
print 'length: %d' % len(d2)   # 字典的长度
print d2['name']     # 定位name键上的值
d2['name'] = 'nam'    # 给name键赋值
print d2
if 'name' in d2:   # 判断 name键是否存在    判断的是键不是值
    print(123)
print d2
# 通过模板方式对字符串中的变量进行输出，注意字符串中的变量
template = '''<html><head>
<title>%(title)s</title></head>
<body>%(body)s
<p>%(body)s</p>
</body>
</html>
'''
#  -------clear 方法
dic = {'title': 'hello word', 'body': 'its the body'}
print template % dic
dic.clear()   # 清空所有的内容
# print dic
dic['title'] = 'ni hao'  # 字典中直接添加内容
dic['body'] = 'this is body'
# print dic
# -------copy 方法   潜复制  复制后值本身是一样的  尝试使用deepcopy
dic_copy = dic.copy()
dic_copy['body'] = 'hello world'
print dic
print dic_copy
# --------fromkeys方法  使用给定的键建立字典，值默认为空
{}.fromkeys(['name', 'age'])
# 或者
dic_from = dict.fromkeys(['name', 'age'])
print dic_from

# --------get方法    为空时返回none  其他方法会返回错误
print dic_from.get('agg', 'agg不存在')  # get 的两个参数，前面为要查询的内容，后面为不存在时返回的内容
# --------has_key   检查字典是否有给出的键 存在返回true
print dic_from.has_key('name')
# -------pop 方法  删除指定的键值
dic_from.pop('name')
print dic_from
# --------popitem  删除随机的项
