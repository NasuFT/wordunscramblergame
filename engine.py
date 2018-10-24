import random

def read_file(file):
	"""	Returns a list of words given in a file.
	"""

	f = open(file)

	words = [word.rstrip() for word in f]

	f.close()

	return words

def pick_word(dictionary, index):
	"""	Returns the n-th word from a dictionary with n = index.
	"""

	return dictionary[index]

def scrabble_score(string):
	"""	Returns the scrabble score from a given string.
	"""

	string = string.lower()
	score = 0
	scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,\
		1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

	for char in string:
		index = ord(char) - ord('a')
		score += scores[index]

	return score

def max_scrabble_score(dictionary, string, length = 0):
	"""	Returns the highest possible score given a word and its unscrambled
		words with length of at least n letters (given length = n, 
		defaults to 0) from a given dictionary. 
	"""
	
	words = search_anagrams(dictionary, string, length = length)
	max_score = 0

	for word in words:
		max_score += scrabble_score(word)

	return max_score

def check_word(string, word):
	"""	Returns True if the second word can be found using letters in the
		first word, otherwise False.
	"""

	count = 0

	for char in word:
		if char in string:
			index = string.index(char)
			string = string[:index] + string[index + 1:]
			count += 1

	if count == len(word):
		return True
	else:
		return False

def search_anagrams(dictionary, string, length = 0):
	"""	Returns a list of all words that can be formed from a word
		from a given dictionary.
		Only returns anagrams of at least n length
		(given length = n, defaults to 0).
	"""

	words = []

	for word in dictionary:
		if check_word(string, word):
			if len(word) < length:
				continue
			words.append(word)

	return words

def combine_words(iterable):
	"""	Returns the shortest string that can be formed from a given
		list of words. The string will be in alphabetical order.
	"""

	min_word = [0] * 26
	combined_word = ""

	for i in iterable:
		letter_count = [0] * 26

		for letter in i:
			index = ord(letter) - ord('a')
			letter_count[index] += 1

		for j in range(26):
			if(min_word[j] < letter_count[j]):
				min_word[j] = letter_count[j]

	for i in range(26):
		if min_word[i] == 0:
			continue

		char_key = ord('a') + i
		combined_word += chr(char_key) * min_word[i]

	return combined_word

def seed(seed):
	"""	Sets the random seed for use in other random functions.
	"""

	if seed != "":
		random.seed(seed)
	else:
		random.seed()

def anagram_random(dictionary, min_length, max_length):
	"""	Returns a random word from a given dictionary
		with length in range [min_length, max_length].
	"""

	word = random.choice(dictionary)

	while not min_length <= len(word) <= max_length:
		word = random.choice(dictionary)

	return word

def combine_random(dictionary, min_size, max_size, min_length, max_length):
	"""	Returns a list of random size in range [min_size, max_size] with words
	of length in range [min_length, max_length].
	"""

	words = []

	for i in range(random.randint(min_size, max_size)):
		x = random.choice(dictionary)

		while min_length <= len(x) <= max_length:
			x = random.choice(dictionary)

		words.append(x)

	return words


class AnagramMode:
	""" Creates a class specifically for Anagram Game Mode.
	"""

	def __init__(self, dictionary, mode):
		self.dictionary = dictionary
		self.min_length = 3
		self.max_length = 9
		self.score = 0
		self.word = anagram_random(dictionary, self.min_length,
											   self.max_length)
		self.anagrams = search_anagrams(dictionary, self.word,
										length = self.max_length)
		self.anagrams_check = self.anagrams[:]

		if mode == "zen":
			self.lives = 3



	def is_correct(self, string):
		if check_word(self.dictionary, string) and string in self.anagrams:
			return True
		else:
			return False






if __name__ == "__main__":
	dictionary = read_file('dictionary.txt')
	score = max_scrabble_score(dictionary, 'rnpcemtreaserfsno', length = 3)
	print(score)
	print(combine_words(['art', 'acts', 'refresh']))
	print(combine_words(['happens', 'woops', 'inhales', 'antickt', 'rool']))