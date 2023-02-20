import json
import os

# (   os.path.dirname(os.path.abspath(__file__)) +"data/company_number.json")

with open("data/company_number.json", "r") as f:
    company_number = json.loads(f.read())

for i in company_number:
    with open("data/candlestick/day_1_candlestick/"+str(i)+".json", "r") as f:
        day_1_candlestick = json.loads(f.read())
    for j in range(len(day_1_candlestick["ta"])-5):
        total = 0
        time = day_1_candlestick["ta"][j+5]["c"]
        for k in range(5):
            total += day_1_candlestick["ta"][j+k]["c"]
        MA5 = total/5
        if os.path.isfile("data/technical_indicator/EMA/MA5"+str(i)+".json"):
            with open("data/technical_indicator/EMA/MA5"+str(i)+".json", "r+") as f:
                temp_data = json.loads(f.read())
                temp_data += dict(time, MA5)
                f.write(str(temp_data))
            # data_1_candlestick_path = os.path.abspath(i)
            # print(os.path.abspath())

1 2 3 4 5 6
0 1 2 3 4 5
0-4
