# -*- coding:utf-8 -*-
from simhash import Simhash
import jieba
import jieba.analyse
# 求两篇文章相似度
def simhash_similarity(text1, text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)
    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    #print(max_hashbit)

    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)
    #print(distince)

    similar = 1 - distince / max_hashbit
    return similar

if __name__ == '__main__':
    f = open('C:/Users/dell/Desktop/sim_0.8/orig.txt', 'rt' ,encoding='utf-8')
    g = open('C:/Users/dell/Desktop/sim_0.8/1.txt', 'rt',encoding='utf-8')
    i = open('C:/Users/dell/Desktop/sim_0.8/2.txt', 'rt', encoding='utf-8')
    j = open('C:/Users/dell/Desktop/sim_0.8/3.txt', 'rt', encoding='utf-8')
    k = open('C:/Users/dell/Desktop/sim_0.8/4.txt', 'rt', encoding='utf-8')
    l = open('C:/Users/dell/Desktop/sim_0.8/5.txt', 'rt', encoding='utf-8')
    m = open('C:/Users/dell/Desktop/sim_0.8/6.txt', 'rt', encoding='utf-8')
    n = open('C:/Users/dell/Desktop/sim_0.8/7.txt', 'rt', encoding='utf-8')
    p = open('C:/Users/dell/Desktop/sim_0.8/8.txt', 'rt', encoding='utf-8')
    q = open('C:/Users/dell/Desktop/sim_0.8/9.txt', 'rt', encoding='utf-8')
    f1 = f.read()
    g1 = g.read()
    g2 = i.read()
    g3 = j.read()
    g4 = k.read()
    g5 = l.read()
    g6 = m.read()
    g7 = n.read()
    g8 = p.read()
    g9 = q.read()
    similar = simhash_similarity(f1,g1 )
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g2)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g3)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g4)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g5)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g6)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g7)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g8)
    print("%.2f" % similar)
    similar = simhash_similarity(f1, g9)
    print("%.2f" % similar)
