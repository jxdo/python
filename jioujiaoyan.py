# coding:gbk
import hashlib
__author__ = 'Administrator'
chararray = [0, 1]
for char1 in chararray:
    for char2 in chararray:
        for char3 in chararray:
            for char4 in chararray:
                for char5 in chararray:
                    for char6 in chararray:
                        for char7 in chararray:
                            for char8 in chararray:
                                for char9 in chararray:
                                    for char10 in chararray:
                                        for char11 in chararray:
                                            for char12 in chararray:
                                                str_out = str(char1)+str(char2)+str(char3)+str(char4)+str(char5)+str(char6)+str(char7)+str(char8)+str(char9)+str(char10)+str(char11)+str(char12)
                                                m = hashlib.md5()
                                                m.update(str_out)
                                                psw = m.hexdigest()
                                                print psw


