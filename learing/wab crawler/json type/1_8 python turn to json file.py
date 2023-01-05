import json

dictObj ={"s":"20","sb":"87"}

fn = 'out1_8.json'                  #file name
with open(fn,'w') as fnObj:
    json.dumps(dictObj,fnObj)#anyother write : fnobj = json.dump(dictObj) ***no dumps
    