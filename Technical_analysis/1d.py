import json
import pandas as pd
import yfinance


with open('1101.json') as f:
    temp_data = json.load(f)
m1 = temp_data["basicin_formation"]["candlestick"]["1m"] 

#temp_data = {"basicin_formation":{"candlestick":{"1m":[m1],"5m":[]}}}

try:
    d1 = temp_data["basicin_formation"]["candlestick"]["d1"]
    final_d1_time = d1[-1]["t"]
 
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) / 2  #取中間索引的值
        if data[mid] < final_d1_time:    #若搜尋值比中間的值大，將中間索引+1，取右半
            low = mid + 1
        elif data[mid] > final_d1_time:  #若搜尋值比中間的值小，將中間索引+1，取左半
            upper = mid - 1
        else:                    #若搜尋值等於中間的值，則回傳
            target_m1_time_index = mid
            
    while int(m1[target_m1_time_index]["t"])%10000 == int(final_d1_time):
        target_m1_time_index+=1
    target_d1_time = str(int(m1[target_m1_time_index]["t"])%10000)

    max = 0
    min = 200000
    while(m1[target_m1_time_index]["t"])
        if m1[i]["h"]>max:
            max = m1[i]["h"]
        if m1[i]["l"]>max:
            max = m1[i]["h"]    
    

except:
     
