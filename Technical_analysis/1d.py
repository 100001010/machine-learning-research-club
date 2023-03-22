import json
import pandas

with open('1101.json') as f:
    temp_data = json.load(f)
m1 = temp_data["basicin_formation"]["candlestick"]["1m"] 

max =0
min =200000
for i in range(-270,0):
    if m1[i]["h"]>max:
        max = m1[i]["h"]
    if m1[i]["l"]<min:
        min = m1[i]["h"]
    