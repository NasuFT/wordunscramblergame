import time

import engine
import interface


dictionary = engine.read_file("dictionary.txt")

while True:
	# ------ GAME LAUNCH ------
	interface.start_game()
	gmode = interface.select_gmode()  # Select Game Mode
	interface.gmode_start(gmode)

	mode = interface.select_mode()  # Select Mode

	if not interface.confirm("START GAME? [Y/n]: "):  # Game Start Confirmation
		continue

	# Randomization
	engine.seed(interface.read_input("Enter seed (Leave blank if unsure): "))

	# ------ GAME START ------

	if gmode == "anagram":
		game = engine.AnagramMode(dictionary)
	elif gmode == "combine":
		game = engine.CombineMode(dictionary)

	interface.chosen_word(game.word)

	while game.lives > 0:
		guess = interface.read_input()
		_is_correct = game.is_correct(guess)
		
		if guess[0:2] == "c_":  # If user typed a command
			if guess == "c_help":
				interface.help()
			elif guess == "c_word":
				interface.chosen_word(game.word)
		elif len(guess) < 3:  # If user typed a word with less than 3 letters
			interface.short_word(3)
		elif _is_correct:  # If user is correct
			if _is_correct == "guessed":  #If already guessed
				interface.guessed()
			else:
				interface.correct()
				if gmode == "combine":
					interface.chosen_word(game.word)
		else:  # If user is wrong
			interface.retries(game.lives)

	# ------ POST GAME ------
	interface.calculate_score(game.score)

	if not interface.confirm("Play Again? [Y/n]: "):
		interface.on_exit()
		time.sleep(3)
		break



