import json

with open('/Users/apple/Documents/github/machine learning research club/Technical_analysis/test.json') as fnobj:
    data = json.load(fnobj)

for i in range(len(data["ta"])):
    print(data["ta"][i]["v"])

# EMA
