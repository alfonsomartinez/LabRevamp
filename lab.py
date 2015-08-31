#######################
# Utilities Functions #
#######################

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_to_num = {char:i for i,char in enumerate(alphabet)}
num_to_letter = {i:char for i,char in enumerate(alphabet)}

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    if not lst:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    for i in range(len(lst)):
        lst[i] = fn(lst[i])


#########################
# Create Vigenere Board #
#########################

def create_row(start, stop):
	""" Create a single row in the Vigenere Board, where start is the 
	number of the letter in the alphabet where you wish to start and stop
	is the number of the previous letter to indicate where to stop the cycle.
	0 = 'A', 1 = 'B' ... 25 = 'Z'

	"""
	row, counter = [], 1
	while counter <= 26:
		if start == 26:
			start = 0
		row += [num_to_letter[start]]
		counter, start = counter + 1, start + 1
	return row

def create_board():
	""" Using create_row to make each different row inside of one list. 
	The final output should be a list of lists where every list is a different 
	row of the Vigenere Board.

	"""
	board = []
	for index in range(26):
		board += [create_row(index, index - 1)]
	return board

cipher = create_board() # Create the Viginere Board

###################
# Encrypt Message #
###################

def encrypt(message, board, key):
	""" Encrypt by creating a new string where you map each letter form
	its original position, to what letter is in its place in the row.
	
	Ex: cipher[5] =  ['F', 'G', 'H', 'I', ... 'E']
	'A' -> 'F'
	'B' -> 'G'
	'C' -> 'H'
	...
	'Z' -> 'E'

	"""
	message = message.upper() # Capitalize Everything 
	key = key.upper() # Capitalize Everything
	row = get_row(board, key)
	string = ''
	for letter in message:
		if letter == ' ':
			string += ' '
		else:
			i = letter_to_num[letter]
			string += row[i]
	return string

###################
# Decrypt Message #
###################

def decrypt(message, board, key):
	""" Decrypt the message by first retrieving the row used to encrypt the
	message, using the key provided and creating a new string where you map
	every letter by looking at the letter that currently takes its place in
	the alphabet.

	Ex: cipher[5] = ['F', 'G', 'H', 'I', ... , 'E']
		1. 'F' is index 0 of the current row. The 0 letter in the alphabet
		should be 'A'. This means all 'A's were mapped to 'F's if we used
		cipher[5] as our row.

		2. 'Z' is at index 25 of the current row. The letter at index 25 of
		alphabet should be 'Z'. This means all 'Z's were mapped to 'E's during
		the encryption process.

	"""
	message = message.upper() # Capitalize Everything
	key = key.upper() #Capitalize Everything
	row = get_row(board, key)
	string = ''
	for letter in message:
		if letter == ' ':
			string += ' '
		else:
			string += get_letter(row, letter)
	return string

def get_row(board, key):
	""" Retrieve the row you need based on the key. The key will be 
	the first letter in your message and provided for all examples.

	"""
	return board[letter_to_num[key]]

def get_letter(row, letter):
	""" Retrieve the letter that was replaced during the encryption
	by retrieving the index at which the letter should be, then use the
	dictionary 'num_to_letter' to retrive the letter that should be at 
	that index.

	"""
	for i in range(len(row)):
		if row[i] == letter:
			return num_to_letter[i]


#####################################
# Do Not Change Any Line Below Here #
#####################################

# import csv

# results = []
# with open('lab.txt') as inputfile:
# 	for line in inputfile:
# 		results.append(line.strip().split(','))

# results = flatten(results)
# result = " ".join(results)

# final = decrypt(result, cipher, 'K')

# text_file = open('lab_output.txt', 'w')
# for item in final:
# 	text_file.write(item)
# text_file.close()



























