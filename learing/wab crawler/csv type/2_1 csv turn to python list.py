import csv 

fn = '/Users/apple/Documents/github/machine-learning-research-club/learing/wab crawler/csv type/csvReport.csv'
with open (fn) as csvObj :
    listObj = csv.reader (list (csvObj))
    print(listObj)
