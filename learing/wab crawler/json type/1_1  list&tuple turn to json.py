import json

listNumbers = [1,3,2,5]
tupleNumbers = (1,5,6,3)

jsonData1 =  json.dumps(listNumbers)
jsonData2 = json.dumps(tupleNumbers)

print("list turn to json",jsonData1,"->",jsonData2)
print("tuple turn to json",listNumbers,"->",tupleNumbers)
print("*datatype of json array is",type(jsonData2),"in json")