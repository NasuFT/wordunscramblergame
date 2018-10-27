def file_read(name_of_file):
	file = open(name_of_file)
	Dictionary_l = [i.rstrip() for i in file]
	return Dictionary_l

def word_find(dictonary,index):
	return dictionary[index]

def find_anagram(dictionary,word):
	anagram_l = []
	while i < len(dictionary):			
		if sorted(word) == sorted(dictionary_l[i]):
			anagram.append(dictionary_l[i])
		i = i + 1
	return anagram_l



def scoring(word):
	scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
	i = 0
	score = 0
	while i < len(word):
		index_word = ord(word[i]) - ord('a')
		score = scores[index_word] + score
		i = i + 1
	return score
