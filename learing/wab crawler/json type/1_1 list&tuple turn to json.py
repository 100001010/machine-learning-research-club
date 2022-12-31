import json

listNumbers = [1]
tupleNumbers = (1,5,6,3)

jsonData1 =  json.dumps(listNumbers)
jsonData2 = json.dumps(tupleNumbers)

print("list turn to json :",jsonData1,"->",jsonData2)
print("tuple turn to json :",listNumbers,"->",tupleNumbers)
print("*data type of json array is",type(jsonData1),"in json")
print(type(listNumbers))