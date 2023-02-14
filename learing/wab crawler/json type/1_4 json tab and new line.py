import json

players={'Stephen Curry':'Golden State Warriors',
         'Kavin Durant':'Golden State Warriors',
         'James Harden':'Houston Rockets'
        }

jsonObj1 = json.dumps(players,sort_keys=True,indent=4)
jsonObj2 = json.dumps(players,indent=4,sort_keys=True)
print (jsonObj1)
print (jsonObj1!=jsonObj2)