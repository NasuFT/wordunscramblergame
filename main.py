import engine
import interface
import random
import time

dictionary = engine.read_file("dictionary.txt")

while(True):
	# ------ BEFORE THE GAME STARTS -------

	# ---- Game Launch ----
	interface.start_game()

	# ---- Main Menu ----
	# ---- Select Game Mode ----
	gmode = interface.select_gmode()

	if gmode == "anagram":
		interface.anagram_start()
	elif gmode == "combine":
		interface.combine_start()

	# ---- Select Mode ----

	mode = interface.select_mode()
	if mode == "cancel":
		continue
	
	# ---- Game Start Confirmation ----

	if not interface.game_confirm():
		continue

	# ---- Randomizer ----

	seed = input("Enter seed (Leave blank if unsure): ").rstrip()
	engine.seed(seed)
	
	# ------ DURING THE GAME ------

	score = 0

	if gmode == "anagram":
		# ------GAME MODE: ANAGRAM------

		word = engine.anagram_random(dictionary, 3, 7)
		anagrams = engine.search_anagrams(dictionary, word, length = 3)
		recheck = anagrams[:]

		interface.chosen_word(word)

		if mode == "zen":
			# ------ZEN MODE------

			lives = 3
			interface.retries(lives)

			while(lives > 0):
				guess = interface.read_input()

				if guess in ("c_word", "c_help"):
					# ---- Commands ----

					if guess == "c_word":
						interface.chosen_word(word)
					elif guess == "c_help":
						interface.help()

				elif len(guess) < 3:
					# ---- Word too short ----

					interface.short_word(3)

				elif engine.check_word(word, guess) and guess in anagrams:
					# ---- Check if valid anagram -----

					score += engine.scrabble_score(guess)
					anagrams.remove(guess)
					interface.correct()

				elif guess in recheck:
					# ---- Check if word had been guessed already ----

					interface.guessed()

				else:
					# ---- Remove 1 life ----

					lives -= 1
					interface.retries(lives)

	elif gmode == "combine":
		# ------GAME MODE: COMBINE------

		if mode == "zen":
			# ------ZEN MODE------

			lives = 3
			interface.retries(lives)
			correct = True

			while(lives > 0):

				if correct:
					correct = False

					words = engine.combine_random(dictionary, 3, 6, 4, 7)
					interface.chosen_word(words)

					word = engine.combine_words(words)

				guess = interface.read_input()

				if guess in ("c_help", "c_word"):
					# Commands

					if guess == "c_help":
						interface.help()
					elif guess == "c_word":
						interface.chosen_word(words)

				elif len(guess) < 0:
					# ---- Word too short ----

					interface.short_word(1)

				else:
					# Check if correct answer
					correct = True

					for i in words:
						if not engine.check_word(guess, i):
							correct = False
							break

					if correct:
						score += engine.scrabble_score(guess)
						interface.correct()
					else:
						# Remove 1 life

						lives -= 1
						interface.retries(lives)

	# ------ AFTER THE GAME ------

	interface.calculate_score(score)

	if not interface.play_again():
		interface.on_exit()
		time.sleep(3)
		print("AWAKEN, MY MASTERS")
		time.sleep(0.5)
		break


# ------ TO DO LIST ------
# ---- HIGH PRIORITY ----
# > GUI
# ---- MEDIUM PRIORITY ----
# > TIMERS IN TERMINAL BY THREADING
# ---- LOW PRIORITY ----
# > CLEANING UP INTERFACE.py
# > CLEANING UP MAIN.py