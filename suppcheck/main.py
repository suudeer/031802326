# -*- coding:utf-8 -*-
from sys import argv
import math
import jieba
import jieba.analyse
from simhash import Simhash


class SimHash(object):
    def getBinStr(self, source):
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

    def getWeight(self, source):
        # 带有关键字的权重
        return ord(source)

    def unwrap_weight(self, arr):
        ret = ""
        for item in arr:
            tmp = 0
            if int(item) > 0:
                tmp = 1
            ret += str(tmp)
        return ret

    def simHash(self, rawstr):
        seg = jieba.cut(rawstr)
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=100, withWeight=True)
        ret = []
        for keyword, weight in keywords:
            binstr = self.getBinStr(keyword)
            keylist = []
            for c in binstr:
                weight = math.ceil(weight)
                if c == "1":
                    keylist.append(int(weight))
                else:
                    keylist.append(-int(weight))
            ret.append(keylist)
        # 对列表进行"降维"
        rows = len(ret)
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

    def getDistince(self, hashstr1, hashstr2):
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1
        return length


def textsimlarSimhash(text1, text2):
    simhash = SimHash()
    hash1 = simhash.simHash(text1)
    hash2 = simhash.simHash(text2)
    distince = simhash.getDistince(hash1, hash2)
    aa_simhash = Simhash(hash1)
    bb_simhash = Simhash(hash2)
    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    similar = 1 - distince / max_hashbit
    return (similar)


def sppcheak(argv):
    try:
        f = open(argv[1], 'rt', encoding='utf-8')
        g = open(argv[2], 'rt', encoding='utf-8')
        su = open(argv[3], 'w+', encoding='utf-8')
        f1 = f.read()
        g1 = g.read()
        similar = textsimlarSimhash(f1, g1)
        similar = round(similar, 2)
        strs = "两篇文章(" + argv[1] + " & " + argv[2] + ")\n相似率为："
        su.writelines(strs + str(similar))
        print("两篇文章相似率为：%.2f\n结果已经存入指定文档" % similar)
        f.close()
        g.close()
        su.close()
    except IndexError:
        print("输入错误,请重新输入！")
    except FileNotFoundError:
        print("没找到文件，输入错误,请重新输入！")
    return 0


# python main.py C:/Users/dell/Desktop/sim_0.8/orig.txt C:/Users/dell/Desktop/sim_0.8/orig_0.8_add.txt C:/Users/dell/Desktop/sim_0.81/orig_0.8_del.txt
if __name__ == '__main__':
    sppcheak(argv)