import json

players={'Stephen Curry':'Golden State Warriors',
         'Kavin Durant':'Golden State Warriors',
         'James Harden':'Houston Rockets'
        }
jsonSort=json.dumps(players)
jsonNoSort=json.dumps(players,sort_keys=True)

print("used sort_key",jsonSort)
print("unused sort_key",jsonNoSort)
print("both of datatype is same ?" ,jsonNoSort==jsonSort )