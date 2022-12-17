import json

listObj=[{'name':'peter','age':'25','gender':'M'}]
jsonData=json.dumps(listObj)
print("list of dict turn to json",listObj,"->",jsonData)
print("data type of json array is",type(jsonData),"in python")
print(type(listObj))