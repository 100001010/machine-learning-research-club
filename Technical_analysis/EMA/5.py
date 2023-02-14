import json
import os

with open('/Users/apple/Documents/github/machine learning research club/Technical_analysis/test.json') as fnobj:
    data = json.load(fnobj)

a = "test"
b = ".json"
c = a+b

print(os.path.abspath(c))
