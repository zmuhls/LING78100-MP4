# MP4 Spec: Matching

def match_doubles(path: str):
	import re
	collection = []
	with open(path, "r") as source:
		for lines in source:
			entry = lines.rstrip()
			match = re.search(r'(\w)\1+', entry)
			if match:
				collection.append(entry)
	return collection

results = match_doubles('wordlist.txt')
assert len(results) == 197
assert results[0] == 'bottler'
assert results[196] == 'volunteers'
print(results)