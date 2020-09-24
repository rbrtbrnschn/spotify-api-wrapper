#!/bin/python3
import sys,json;
options = ["tracks","albums","artists","playlists","shows","episodes"]
raw = json.load(sys.stdin);
for option in options:
	try:
		first = raw[option]['items'][0]['uri'];
		print(first)
	except:
		print()
#print(json.dumps(first, indent=4, sort_keys=True));
