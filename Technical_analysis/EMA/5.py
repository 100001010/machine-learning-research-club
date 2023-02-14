import json
import os

# (   os.path.dirname(os.path.abspath(__file__)) +"data/company_number.json")

with open("data/company_number.json", "r") as f:
    company_number = json.loads(f.read())

for i in company_number:
    with open("data/candlestick/day_1_candlestick/"+str(i)+".json", "r") as f:
        day_1_candlestick = json.loads(f.read())
    for j in range(len(day_1_candlestick["ta"])):
        total = 0
        for k in range(4):
            total += day_1_candlestick["ta"][j+k]["c"]
        MA5 = total/5
        with open("data/technical_indicator/EMA/MA5"+str(i)+".json", "r") as f:

            # data_1_candlestick_path = os.path.abspath(i)
            # print(os.path.abspath())
