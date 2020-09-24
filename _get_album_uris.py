#!/bin/python3

import sys, json;
raw = json.load(sys.stdin)
tracks = raw['items']
uris = []
for track in tracks:
	uris.append(track['uri'])

print(" ".join(uris))
