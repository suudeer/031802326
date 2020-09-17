# -*- coding:utf-8 -*-
from sys import argv
import math
import jieba
import jieba.analyse
from simhash import Simhash


class SimHash(object):
    def sgetbinStr(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            return str(x)

    def simHash(self, rawstr):
        seg = jieba.cut(rawstr)
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        ret = []
        for keyword, weight in keywords:
            binstr = self.sgetbinStr(keyword)
            keylist = []
            for c in binstr:
                weight = math.ceil(weight)
                if c == "1":
                    keylist.append(int(weight))
                else:
                    keylist.append(-int(weight))
            ret.append(keylist)
        rows = len(ret)  # 对列表进行"降维"
        cols = len(ret[0])
        result = []
        for i in range(cols):
            tmp = 0
            for j in range(rows):
                tmp += int(ret[j][i])
            if tmp > 0:
                tmp = "1"
            elif tmp <= 0:
                tmp = "0"
            result.append(tmp)
        return "".join(result)


def textsimlarSimhash(text1, text2):
    simhash = SimHash()
    hash1 = simhash.simHash(text1)#计算hash
    hash2 = simhash.simHash(text2)#计算hash
    t1_simhash = Simhash(hash1)
    t2_simhash = Simhash(hash2)
    distince = t1_simhash.distance(t2_simhash)
    max_hashbit = max(len(bin(t1_simhash.value)), (len(bin(t2_simhash.value))))
    if max_hashbit == 0:
        return 0
    else:
        ssimilar = 1 - distince / max_hashbit
        return (ssimilar)


def sppcheak(argv):
    try:
        f = open(argv[1], 'rt', encoding='utf-8')#打开源文件
        g = open(argv[2], 'rt', encoding='utf-8')#打开检测文件
        su = open(argv[3], 'w+', encoding='utf-8')
        f1 = f.read()#读取文件--字符串
        g1 = g.read()#读取文件--字符串
        similar = textsimlarSimhash(f1, g1)#计算相似度
        similar = round(similar, 2)#保留小数
        strs = "两篇文章(" + argv[1] + " & " + argv[2] + ")\n相似率为："
        su.writelines(strs + str(similar))
        print("两篇文章相似率为：%.2f\n结果已经存入指定文档" % similar)
        f.close()
        g.close()
        su.close()#关闭文件
    except IndexError:
        print("输入错误,请重新输入！")
    except FileNotFoundError:
        print("没找到文件，输入错误,请重新输入！")
    return 0


# python main.py C:/Users/dell/Desktop/sim_0.8/orig.txt C:/Users/dell/Desktop/sim_0.8/orig_0.8_add.txt C:/Users/dell/Desktop/sim_0.81/orig_0.8_del.txt
if __name__ == '__main__':
    sppcheak(argv)
