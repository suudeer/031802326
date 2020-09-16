# -*- coding:utf-8 -*-
from simhash import Simhash


# 求两篇文章相似度
def simhash_similarity(text1, text2):
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)
    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    # 汉明距离
    distinces = aa_simhash.distance(bb_simhash)
    similar = 1 - distinces / max_hashbit
    return similar


f = open('orig.txt', 'rt', encoding='utf-8')
f1 = f.read()
# 第零组
similar = simhash_similarity(f1, f1)
print("orig.txt 与 orig.txt 的相似度为：%.2f" % similar)
# 第一组
g = open('orig_0.8_add.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_add.txt 的相似度为：%.2f" % similar)
g.close()
# 第二组
g = open('orig_0.8_del.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_del.txt 的相似度为：%.2f" % similar)
g.close()
# 第三组
g = open('orig_0.8_dis_1.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_dis_1.txt 的相似度为：%.2f" % similar)
g.close()
# 第四组
g = open('orig_0.8_dis_3.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_dis_3.txt 的相似度为：%.2f" % similar)
g.close()
# 第五组
g = open('orig_0.8_dis_7.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_dis_7.txt 的相似度为：%.2f" % similar)
g.close()
# 第六组
g = open('orig_0.8_dis_10.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_dis_10.txt 的相似度为：%.2f" % similar)
g.close()
# 第七组
g = open('orig_0.8_dis_15.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_dis_15.txt 的相似度为：%.2f" % similar)
g.close()
# 第八组
g = open('orig_0.8_mix.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_mix.txt 的相似度为：%.2f" % similar)
g.close()
# 第九组
g = open('orig_0.8_rep.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_rep.txt 的相似度为：%.2f" % similar)
g.close()
# 第十组
g = open('orig_0.8_self.txt', 'rt', encoding='utf-8')
g1 = g.read()
similar = simhash_similarity(f1, g1)
print("orig.txt 与 orig_0.8_self.txt 的相似度为：%.2f" % similar)
g.close()
f.close()
