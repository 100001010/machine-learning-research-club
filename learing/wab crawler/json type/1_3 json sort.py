import json

players={'Stephen Curry':'Golden State Warriors',
         'Kavin Durant':'Golden State Warriors',
         'James Harden':'Houston Rockets'
        }
jsonSort=json.dumps(players,sort_keys=True)
jsonNoSort=json.dumps(players)

print("used sort_key",jsonSort)
print("unused sort_key",jsonNoSort)
print("both of object is same ?" ,jsonNoSort==jsonSort )