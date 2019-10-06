datas = list(map(str,input().split()))

count = 0

for i in range(len(datas)):
    if datas.count(datas[i-1]) < datas.count(datas[i]):
        count = i
        
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(datas[count],datas.count(datas[count])))