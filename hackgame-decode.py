# coding:gbk
__author__ = '1'
decode_str = '1c10121a181e121a0f1016110b4d4d4d'
output=''
for start in range(0, len(decode_str), 2):
    hex_num = decode_str[start:start+2]
    hex_num = int(hex_num, 16)  # 16����ת10����
    hex_num = 255 - hex_num
    # ��Ŀ��<128�ļ�����128���ͱ�128���ˣ���Ҫ�жϴ���128�ļ�ȥ128
    if hex_num > 128:
        hex_num = hex_num - 128
        output += chr(hex_num)
    # ��Ŀ��>127�ļ�ȥ��128���ͱ�128С�ˣ���Ҫ�ж�С��128�ļ���128
    else:
        hex_num = hex_num + 128
        output += chr(hex_num)
print output