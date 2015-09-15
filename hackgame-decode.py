# coding:gbk
__author__ = '1'
decode_str = '1c10121a181e121a0f1016110b4d4d4d'
output=''
for start in range(0, len(decode_str), 2):
    hex_num = decode_str[start:start+2]
    hex_num = int(hex_num, 16)  # 16进制转10进制
    hex_num = 255 - hex_num
    # 题目中<128的加上了128，就比128大了，就要判断大于128的减去128
    if hex_num > 128:
        hex_num = hex_num - 128
        output += chr(hex_num)
    # 题目中>127的减去了128，就比128小了，就要判断小于128的加上128
    else:
        hex_num = hex_num + 128
        output += chr(hex_num)
print output