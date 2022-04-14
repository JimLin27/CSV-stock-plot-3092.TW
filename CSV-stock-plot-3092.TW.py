"""
範例程式: CSV-3092.TW
撰寫時間: 2022/4/13
作者: LIN
功能: 課堂練習
"""
import matplotlib.pyplot as plt
import csv

listOpen=[]
listClose=[]
listHigh=[]
listLow=[]
listDate=[]
volume=[]

with open("3092.TW.csv","r",encoding="utf-8") as fin:
    dataCSV=csv.reader(fin,delimiter=",")   # 用逗號區分資料
    header = next(dataCSV)  # 讀取欄位名稱
    print(header)

    for row in dataCSV:
        listDate.append(row[0])
        listOpen.append(float(row[1]))
        listHigh.append(float(row[2]))
        listLow.append(float(row[3]))
        listClose.append(float(row[4]))
        volume.append(int(row[6]))

x = 0
def highprice(x):
    highPrice = 0
    for i in range(1,len(listDate)):
        if highPrice < listHigh[i]:
            highPrice = listHigh[i]
            x=i
    return x
print("日期:",listDate[highprice(x)],"\n"+
      "最高價格:",listHigh[highprice(x)],"\n"+
      "交易量:",volume[highprice(x)])


y = 0
def highprice(y):
    lowPrice = 1000
    for i in range(1,len(listDate)):
        if listHigh[i]<lowPrice:
            lowPrice = listHigh[i]
            y=i
    return y

print("日期:",listDate[highprice(y)],"\n"+
      "最低價格:",listLow[highprice(y)],"\n"+
      "交易量:",volume[highprice(y)])

total=0
k=0
while k < len(listDate):
    total=total+listOpen[k]
    k+=1
print("平均:",total/len(listOpen))


# 3. 畫出圖表
plt.plot(listHigh, 'r-')
plt.plot(listOpen, 'k-')
plt.plot(listLow, 'b-')
plt.title('3092.TW')
plt.show()
