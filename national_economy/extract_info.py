# -*- coding:utf-8 -*-
# Author：kottravey
# Date: 2020-02-03 21:43

import re
from jpype import JString

from pyhanlp import *

def read_file(FILE_READ_PATH):
    fR = open(FILE_READ_PATH, 'r', encoding='UTF-8')
    contents = fR.read()
    return contents
    fR.close()

def write_file(write_items, FILE_WRITE_PATH):
    fW = open(FILE_WRITE_PATH, 'w', encoding='UTF-8')
    fW.write(write_items)
    fW.close()

if __name__ == '__main__':
    #text = "把招商引资作为扩大对外开放的重点来抓，利用外资取得重大进展，实际利用外资达20.17亿美元，增长54.7％，其中外商直接投资15.61亿美元，增长47.5％。"
    text = read_file("/Users/sadielin/Documents/programmer/nlp/cut/hb.txt")
    sent_lists = ""

    #分词
    segment=HanLP.newSegment().enableCustomDictionary(True)
    termlist = segment.seg(text)
    print("分词结果：", termlist)

    #打印特定词性的词，以及文档拼合
    """
    for i in termlist:
        sent_lists = sent_lists + str(i)
        if str(i.nature) == "nz" :
            print(str(i.word), str(i.nature))
    """

    #单句匹配，搜出nz，m，q，n词性的单词并打印

    for i in termlist:
        #psb 即 possibility
        psb1 = (str(i.nature) == "nz")
        psb2 = (str(i.nature) == "m")
        psb3 = (str(i.nature) == "q")
        psb4 = (str(i.nature) == "n")
        psb5 = (str(i.word) == "%")
        psb6 = (str(i.word) == "％")
        if psb1 or psb2 or psb3 or psb4 or psb5 or psb6:
            sent_lists = sent_lists + str(i.word)
        elif (str(i.word) == "，"):
            sent_lists = sent_lists + str("\n")
        elif (str(i.word) == "、"):
            sent_lists = sent_lists + str("\n")
        elif (str(i.word) == "。"):
            sent_lists = sent_lists + str("\n") + str("\n")
        elif(str(i.word) == "增长"):
            sent_lists = sent_lists + str("+")
        elif(str(i.word) == "减少"):
            sent_lists = sent_lists + str("-")
    print(sent_lists)

    write_file(sent_lists, "/Users/sadielin/Documents/programmer/nlp/cutphrase/cutphhb.txt")
