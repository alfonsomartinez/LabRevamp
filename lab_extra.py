from lab import *
import csv

############################
# Import Encrypted Message #
############################

results = []
with open('input.txt') as inputfile:
	for line in inputfile:
		results.append(line.strip().split(','))

results = flatten(results) # Create list of strings of words
result = " ".join(results) # Join all words as one string

#######################
# Decrypt the Message #
#######################

final = decrypt(result, cipher, 'H')

############################
# Export Decrypted Message #
############################

text_file = open('output.txt', 'w')
for item in final:
	text_file.write(item)
text_file.close()


