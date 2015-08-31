from lab import *
import csv

############################
# Import Encrypted Message #
############################

results = []
with open('lab_extra.txt') as inputfile:
	for line in inputfile:
		results.append(line.strip().split(','))

results = flatten(results) # Create list of strings of words
result = " ".join(results) # Join all words as one string

#######################
# Decrypt the Message #
#######################

def encrypt(message, board, key):
	""" Write a new ecnrypt that takes in a key that Change
	be longer than one letter. For Every letter in the message,
	use the corresponding letter in the word to indicate which row
	to use. Once you reach the end of the key, restart from the first
	letter.

	"""
	message, key = message.upper(), key.upper()
	row = get_row(board, key[0])
	string, word = '', key
	while message:
		if message[0] == ' ':
			string += ' '
			message = message[1:]
		else:
			num = letter_to_num[message[0]]
			string += row[num]
			word = word[1:]
			if not word:
				word = key
			row = get_row(board, word[0])
			message = message[1:]
	return string

def decrypt(message, board, key):
	return

a = encrypt('hello there', cipher, 'denero')

# Do not Change the following line
# final = encrypt(result, cipher, 'DENERO')

############################
# Export Decrypted Message #
############################

text_file = open('lab_extra_output.txt', 'w')
for item in final:
	text_file.write(item)
text_file.close()


