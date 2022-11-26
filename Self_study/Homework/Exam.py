import operator

trainTuList=[('토마스',10),('헨리',8),('에드워드',7),('에밀리',7),('칼리',3),('헨리',3),
            ('에드워드',3),('에밀리',3),('칼리',3),('칼리',5),('칼리',3)]

trainDic, trainList= {}, []
tmpTup= None
totalRank, currentRank=1,1

if __name__ == "__main__":
    for tmpTup in trainTuList:
        tName= tmpTup[0]
        tWeight= tmpTup[1]
        if tName in trainDic: # Key는 고정되니까 수송량만 더하기
            trainDic[tName]+=tWeight
        else:
            trainDic[tName]=tWeight

    #print('기차 수송량 목록 => ', trainTuList)
    print('-------------------')
    trainList= sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True)
    # 딕셔너리를 튜플 형태로
    # itemgetter(1) : 키를 [1]을 기준으로 정렬
    print(trainList)
    print('기차  \t총수송량\t순위')
    print('-------------------')
    print(trainList[0][0],'\t',trainList[0][1],'\t',currentRank) # 1순위 출력
    for i in range(1, len(trainList)):
        totalRank+=1
        if trainList[i][1]== trainList[i-1][1]:
            pass
        else:
            currentRank= totalRank
        print(trainList[i][0],'\t',trainList[i][1],'\t',currentRank)