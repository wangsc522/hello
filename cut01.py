# -*- coding: utf-8 -*-
def getGameData(dataMainDir,userAccount):
    import os, codecs
    mainDir = os.listdir(dataMainDir)
    csvData=[]
    for fileDir in mainDir:
        files = os.listdir("%s/%s" % (dataMainDir,fileDir))
        data = []
        for file in files:
            with codecs.open("%s/%s/%s" % (dataMainDir,fileDir,file) ,"r",  'UTF-8') as f:
                doc=f.readlines()
                #data.append(doc[1].strip().strip("\[").strip("\]").split("=")[1])
                temp=doc[3].strip().strip("\[").strip("\]").split("=")[1].split("：")
                data.append(temp[0])
                data.append(temp[1])
                data.append(doc[4].strip().strip("\[").strip("\]").split("=")[1].split(" ")[1])
                temp=doc[5].strip().strip("\[").strip("\]").split("=")[0].split(" ")
                data.append(temp[0])
                data.append(temp[2])
                data.append(doc[6].strip().strip("\[").strip("\]").split("=")[1])
                data.append(doc[10].strip().strip("\[").strip("\]").split("=")[1].split(" ")[1].split("數")[0])
                temp=doc[13].strip().strip("\[").strip("\]").split("=")[1].split(" ")
                data.append(temp[0])
                #data.append(temp[1])
                dTime=temp[2].split(":")
                if temp[1] == "下午":
                    dTime[0]=str(int(dTime[0])+12)
                data.append("%s:%s" % (("00"+dTime[0])[-2:],("00"+dTime[1])[-2:]))
                #data.append(doc[14].strip().strip("\[").strip("\]").split("=")[1])
                #data.append(doc[17].strip().strip("\[").strip("\]").split("=")[1])
                #data.append(doc[18].strip().strip("\[").strip("\]").split("=")[1])
                #data.append(doc[23].strip().strip("\[").strip("\]").split("=")[1])
                #data.append(doc[24].strip().strip("\[").strip("\]").split("=")[1])
                if userAccount == doc[24].strip().strip("\[").strip("\]").split("=")[1] :
                    data.append("黑")
                    data.append(doc[18].strip().strip("\[").strip("\]").split("=")[1])
                    data.append(doc[17].strip().strip("\[").strip("\]").split("=")[1])
                else:
                    data.append("白")
                    data.append(doc[24].strip().strip("\[").strip("\]").split("=")[1])
                    data.append(doc[23].strip().strip("\[").strip("\]").split("=")[1])
            csvData.append(data)
    return csvData

def saveGameData(csvData):        
    import pandas as pd
    my_df = pd.DataFrame(csvData)
    my_df.to_csv('output.csv', index=False, header=True,encoding='utf-8')

if __name__ == '__main__':
    import sys,os
    if len(sys.argv) < 2: 
        print ("Usage:", sys.argv[0], "帳號")
        sys.exit(1)       
    else:
        #dataMainDir = "C:/Users/wsc/AppData/Local/VirtualStore/Program Files (x86)/棋城圍棋/Gibo"
        dataMainDir = "%s/VirtualStore/Program Files (x86)/棋城圍棋/Gibo" % os.environ['LocalappData'].replace("\\","/")
        userAccount = sys.argv[1]
        print(dataMainDir)
        saveGameData( getGameData(dataMainDir,userAccount))
