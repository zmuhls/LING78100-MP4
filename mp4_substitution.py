# MP4 Spec: Substitution

def sub_pii(self):
	import regex as re
	pattern = re.compile(r'''
					(?<!\S)(?:
					(?=(-*\d-*){7}(\s|\Z))[\d-]+|
					(?=(-*\d-*){11}(\s|\Z))[\d-]+|
					(?=(-*\d-*){12}(\s|\Z))[\d-]+|
					(?=(-*\d-*){13}(\s|\Z))[\d-]+)
					''', re.VERBOSE)
	nullify = lambda m: re.sub(r'\d', '0', m[0])
	remainder = pattern.sub(nullify, self)
	return remainder

corpus = """In the US, some phone numbers are reserved for fictitious purposes.
For instance, 555-0198 and 1-206-5555-0100 are example fictitious numbers.
There are similar ranges of numbers in the UK, Ireland, and Australia.
In the UK, 044-113-496-1234 is a fictitious number in the Leeds area.
In Ireland, the number 353-020-913-1234 is fictitious.
And in Australia, 061-900-654-321 is a fictitious toll-free number.
911 is a joke."""

test = sub_pii(corpus)
print(test)

#assertion tests
assert '555-0198' not in test 
assert '000-0000' in test 

assert '1-206-5555-0100' not in test
assert '0-000-0000-0000' in test

assert '044-113-496-1234' not in test
assert '000-000-000-0000' in test

assert '061-900-654-321' not in test
assert '000-000-000-000' in test

assert '911' in test