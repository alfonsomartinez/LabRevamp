from encrypt import *
import csv

def flatten(lst):
    if not lst:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

results = []
with open('example.txt') as inputfile:
	for line in inputfile:
		results.append(line.strip().split(','))

results = flatten(results)

result = " ".join(results)

result = result.upper()

final = encrypt(result, example[7])

text_file = open('output.txt', 'w')

for item in final:
	text_file.write(item)
text_file.close()


