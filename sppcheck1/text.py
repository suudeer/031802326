from main import textsimlarSimhash


def testppcheck():
    t1 = open('orig.txt', 'rt', encoding='utf-8')
    text1 = t1.read()
    # 第零组
    similar = textsimlarSimhash(text1, text1)
    print("orig.txt 与 orig.txt 的相似度为：%.2f" % similar)
    # 第一组
    t2 = open('orig_0.8_add.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_add.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第二组
    t2 = open('orig_0.8_del.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_del.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第三组
    t2 = open('orig_0.8_dis_1.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_dis_1.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第四组
    t2 = open('orig_0.8_dis_3.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_dis_3.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第五组
    t2 = open('orig_0.8_dis_7.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_dis_7.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第六组
    t2 = open('orig_0.8_dis_10.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_dis_10.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第七组
    t2 = open('orig_0.8_dis_15.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_dis_15.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第八组
    t2 = open('orig_0.8_mix.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_mix.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第九组
    t2 = open('orig_0.8_rep.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_rep.txt 的相似度为：%.2f" % similar)
    t2.close()
    # 第十组
    t2 = open('orig_0.8_self.txt', 'rt', encoding='utf-8')
    text2 = t2.read()
    similar = textsimlarSimhash(text1, text2)
    print("orig.txt 与 orig_0.8_self.txt 的相似度为：%.2f" % similar)
    t2.close()
    t1.close()
    return 0


testppcheck()
