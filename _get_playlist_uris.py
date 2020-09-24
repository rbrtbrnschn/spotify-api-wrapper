#!/bin/python3

import sys, json;
raw = json.load(sys.stdin)
#print(json.dumps(raw,indent=4,sort_keys=True))
tracks = raw['items']
uris = []
for track in tracks:
	uris.append(track['track']['uri'])

print(" ".join(uris))
