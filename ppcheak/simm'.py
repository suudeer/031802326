# coding=utf-8
class simhash:
    # 构造函数
    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)


    # 生成simhash值
    def simhash(self, tokens):
        # v是长度128的列表
        v = [0] * self.hashbits
        tokens_hash = [self.string_hash(x) for x in tokens]
        for t in tokens_hash:  # t为token的普通hash值
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1  # 查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= 1  # 否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint  # 整个文档的fingerprint为最终各个位>=0的和

    # 求海明距离
    def hamming_distance(self, other):
        # 异或结果
        xorResult = (self.hash ^ other.hash)
        # 128个1的二进制串
        hashbit128 = ((1 << self.hashbits) - 1)
        x = xorResult & hashbit128
        count = 0
        while x:
            count += 1
            x &= x - 1
        return count

    # 求相似度
    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    # 针对source生成hash值
    def string_hash(self, source):
        if source == "":
            return 0
        else:
            result = ord(source[0]) << 7
            m = 1000003
            hashbit128 = ((1 << self.hashbits) - 1)

            for c in source:
                temp = (result * m) ^ ord(c)
                result = temp & hashbit128

            result ^= len(source)
            if result == -1:
                result = -2

            return result




if __name__ == '__main__':
    f = open('C:/Users/dell/Desktop/sim_0.8/orig.txt', 'rt', encoding='utf-8')
    s1 = f.read()
    f.close()
    hash1 = simhash(s1.split())
    f = open('C:/Users/dell/Desktop/sim_0.8/orig_0.8_dis_1.txt', 'rt', encoding='utf-8')
    s2 = f.read()
    f.close()
    hash2 = simhash(s2.split())
    print(hash1.similarity(hash2))
