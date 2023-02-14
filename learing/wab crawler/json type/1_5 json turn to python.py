import json 

jsonObj ='{"b":"80","a":"90","c":150}'#json type is str ,but use " ' " ,not use " " "
pythonObj=json.loads(jsonObj)
print("json turn to python",jsonObj,"->",pythonObj)
print(type(pythonObj))