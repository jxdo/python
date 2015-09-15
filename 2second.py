# coding:utf-8
import requests

s = requests.Session()  # 一定要加session，否则后面post时无法识别是否同一个请求
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url)
html = unicode(r.content, 'utf-8').encode("gbk")
html = r.content
left = html.find("<br/>")
right = html.find(")=")
ss = html[(left+5):(right+1)]
result = eval(ss.strip())                          # 通过定位字符串左右的索引从而可以每次都精确定位到计算字符串
# result = eval(html.split('\n')[8].strip()[0:28])  # 计算结果中的，因每次的计算不同使用固定的28个无法每次精确
print result
data = {'v': result}
res = s.post(url, data)
res = unicode(res.content, 'utf-8')
print res
