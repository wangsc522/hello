# -*- coding: utf8 -*-
# 20170203 計算單詞出現次數,出現次數多者並不具差異性
import codecs,sys
import jieba.analyse
import logging
import os 
import json

def main(dataMainDir):
    import jieba
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #jieba.set_dictionary('jieba_dict/document_taiba.dict.txt')
    jieba.set_dictionary('jieba_dict/userdict.txt')
    #jieba.analyse.set_stop_words('jieba_dict/stopwords.txt')

    #jieba.load_userdict('jieba_dict/userdict.txt')


    mainDir = os.listdir(dataMainDir)
    #fkeyword = open("keyword.csv","w", encoding = 'UTF-8')
    #ret = ''
    #items = ""
    tagList=[99,3,99,4,4,0,4,99,99,99,3,99,4,3,4,99,3,99,99,99,99,99,3]
    #writeData=[[0,0],[1,0],[2,2],[3,0],[3,6],[4,0],[5,4],[7,8],[7,10],[7,11]]
    #tagList=range(6)
    for fileDir in mainDir:
        files = os.listdir("%s/%s" % (dataMainDir,fileDir))
        fgogogo = open("gogogo.csv","w", encoding = 'UTF-8')
        for file in files:
            print("=================%s================" % file)
            fGoData = open("%s/%s/%s" % (dataMainDir,fileDir,file), "r")
            cc=0
            lData = []
            for pos in tagList:
                cc+=1
                goData=fGoData.readline()
                seglist = list(jieba.cut(goData, cut_all=True))
                if pos<99:
                    print( "%s"%cc+  ''.join("%s" % (item)  for item,num in zip(seglist[pos:-1],range(200) )))
                    lData.append(seglist[pos:-1])
#                    if merge==0:
#                        lData.append( ''.join("%s" % (item)  for item in  ))
#                    else:
#                        lData.append( ','.join("%s" % (item)  for item in seglist[pos:-1] ))
            print(lData)
     #       resultData=[]
     #       for col,row in writeData:
                #resultData.append("%s" % lData[col,row])
     #           print( lData[col][row])
            #seglist = list(jieba.cut(goData, cut_all=True))
            #seglist =list(jieba.analyse.extract_tags(goData, 50000))
            #print(' '.join(":%s" % (item)  for item,num in zip(seglist,range(200) )))
            #c=""
            #for item,num in zip(seglist,range(200) ):
                #print(item)
            #    if num in tagList:
            #        c=c+"_"+item
                    #print("%s:%s" % (num,item))
            #for data in goData:
            #print("%s" % c)
    #fkeyword.close()

if __name__ == '__main__':
    dataMainDir = "C:/Users/wsc/AppData/Local/VirtualStore/Program Files (x86)/棋城圍棋/Gibo"
    main(dataMainDir)