# coding:gbk
__author__ = 'Administrator'
# ----------------------------------------------�ֵ䣬�ֵ��������
# �����ֵ�
ems = {'name': 'jxdo', 'age': '22'}
print ems
ems1 = [('name', 'df'), ('ege', '21')]
d2 = dict(ems1)
print 'length: %d' % len(d2)   # �ֵ�ĳ���
print d2['name']     # ��λname���ϵ�ֵ
d2['name'] = 'nam'    # ��name����ֵ
print d2
if 'name' in d2:   # �ж� name���Ƿ����    �жϵ��Ǽ�����ֵ
    print(123)
print d2
# ͨ��ģ�巽ʽ���ַ����еı������������ע���ַ����еı���
template = '''<html><head>
<title>%(title)s</title></head>
<body>%(body)s
<p>%(body)s</p>
</body>
</html>
'''
#  -------clear ����
dic = {'title': 'hello word', 'body': 'its the body'}
print template % dic
dic.clear()   # ������е�����
# print dic
dic['title'] = 'ni hao'  # �ֵ���ֱ���������
dic['body'] = 'this is body'
# print dic
# -------copy ����   Ǳ����  ���ƺ�ֵ������һ����  ����ʹ��deepcopy
dic_copy = dic.copy()
dic_copy['body'] = 'hello world'
print dic
print dic_copy
# --------fromkeys����  ʹ�ø����ļ������ֵ䣬ֵĬ��Ϊ��
{}.fromkeys(['name', 'age'])
# ����
dic_from = dict.fromkeys(['name', 'age'])
print dic_from

# --------get����    Ϊ��ʱ����none  ���������᷵�ش���
print dic_from.get('agg', 'agg������')  # get ������������ǰ��ΪҪ��ѯ�����ݣ�����Ϊ������ʱ���ص�����
# --------has_key   ����ֵ��Ƿ��и����ļ� ���ڷ���true
print dic_from.has_key('name')
# -------pop ����  ɾ��ָ���ļ�ֵ
dic_from.pop('name')
print dic_from
# --------popitem  ɾ���������
