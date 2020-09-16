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
        # fake weight with keyword
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


def textsimlarSimhash(text1,text2):
    simhash = SimHash()
    hash1 = simhash.simHash(text1)
    hash2 = simhash.simHash(text2)
    distince = simhash.getDistince(hash1, hash2)
    aa_simhash = Simhash(hash1)
    bb_simhash = Simhash(hash2)
    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    similar = 1 - distince / max_hashbit
    print("相似度：", similar)


t1=open('C:/Users/dell/Desktop/sim_0.8/orig.txt', 'rt', encoding='utf-8')
text1 = t1.read()
t2= open('C:/Users/dell/Desktop/sim_0.8/orig_0.8_self.txt', 'rt', encoding='utf-8')
text2 = t2.read()

textsimlarSimhash(text1,text2)

