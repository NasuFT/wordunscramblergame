Dictionary_l = []

def file_read(name_of_file):
	global Dictionary_l

	file = open(name_of_file)
	Dictionary_l = [i.rstrip() for i in file]

def word_r_find():
	import random
	index_word = random.randint(0, len(Dictionary_l) - 1)
	word = Dictionary_l[index_word]
	word_r = ''.join(random.sample(word,len(word)))
	return word_r

def check_answers(word1,word2):	
	i = 0
	while i < len(word1):
		if word1[i] in word2:
			if i == len(word1) -1:
				return word1
			i = i + 1
		else:
			return '0'

def correct_answers(word1):
	j = 0
	correct_l = []
	while j < len(Dictionary_l):
		correct = check_answers(Dictionary_l[j], word1)
		if correct != '0':
			correct_l.append(Dictionary_l[j])
		j += 1
	return correct_l

def scoring(word):
	scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
	i = 0
	score = 0
	while i < len(word):
		index_word = ord(word[i]) - ord('a')
		score = scores[index_word] + score
		i = i + 1
	return score

# -------------------- START GAME -----------------------
file_read('dictionary.txt')
given_word = word_r_find()
correct_l = correct_answers(given_word)
lives = 3

print("""
YOU ARE GIVEN: 3 LIVES
UNSCRABLE THE WORD BELOW:
	""")

used_answers = []
total_score = 0

while lives != 0:
	print(given_word)
	answer = input()

	if answer == ' ':
		import random
		given_word = ''.join(random.sample(given_word,len(given_word)))

	else:

		if answer in correct_l:

			if answer in used_answers:
				print(("ENTERED ALREADY"),"\n")

			else:
				used_answers.append(answer)
				print("CORRECT")
				score = scoring(answer)
				total_score += score 
				print("SCORE EARNED : " + str(score),"\n")

				if len(used_answers) == len(correct_l):
					print("""
					YOU FOUND ALL THE WORDS
						CONGRATULATIONS
					""")
					print("TOTAL SCORE : " + str(total_score))

					break

		else:
			lives -= 1
			print("LIVES : " + str(lives))
			print(('WRONG'),"\n")

i = 0
maximum_score = 0

while i < len(correct_l):
	score = scoring(correct_l[i])
	maximum_score += score
	i = i + 1
	
print("TOTAL SCORE : " + str(total_score)+" OUT OF " + str(maximum_score))

print("YOU FOUND " + str(len(used_answers)) + " OUT OF " + str(len(correct_l)))
print(
"""
                     GAME OVER LOSER
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")
