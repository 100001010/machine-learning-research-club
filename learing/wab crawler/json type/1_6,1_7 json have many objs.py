import json

#if json have many obj ,notice grammar
jsonobj = '{"Asia":[{"japan":"tokyoe"},{"taiwan":"taipai"}],"america":[{"usa":"nuya"}]}'
# 4 line anyother grammar
'''
jsonobj = '{"Asia":\                # notic end add "\"
            [{"japan":"tokyoe"},\
             {"taiwan":"taipai"}],\
            "america":\
            [{"usa":"nuya"}]}'\
'''
pythonobj = json.loads(jsonobj)
print(pythonobj)
print(type(pythonobj))
print(pythonobj["Asia"])
print(type(pythonobj["Asia"]))
print(pythonobj["Asia"][0])
print(type(pythonobj["Asia"][0]))
