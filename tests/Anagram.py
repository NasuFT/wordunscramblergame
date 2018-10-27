def file_read(name_of_file):
	file = open(name_of_file)
	Dictionary_l = [i.rstrip() for i in file]

def find_anagram(word):
	anagram_l = []
	while i < len(dictionary_l):			
		if sorted(word) == sorted(dictionary_l[i]):
			anagram.append(dictionary_l[i])
		i = i + 1
	return anagram_l

