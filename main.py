import time

import engine
import interface


dictionary = engine.read_file("dictionary.txt")

while True:
	quit_flag = False
	screen = None

	# ------ GAME LAUNCH ------
	if not screen:
		if interface.confirm("Use Terminal? [Y/n]: "):
			screen = interface.Terminal()
		else:
			pass

	screen.clear()

	screen.start_game()
	gmode = screen.select_gmode()  # Select Game Mode
	screen.gmode_start(gmode)
	
	if not screen.confirm("START GAME? [Y/n]: "):  # Game Start Confirm
		continue

	# Randomization
	engine.seed(screen.read_input("Enter seed (Leave blank if unsure): "))

	# ------ GAME START ------

	if gmode == "anagram":
		game = engine.AnagramMode(dictionary)
	elif gmode == "combine":
		game = engine.CombineMode(dictionary)

	screen.chosen_word(game.word)

	while game.is_alive():
		guess = screen.read_input()
		
		if guess[0:2] == "c_":  # If user typed a command
			if guess == "c_help":
				screen.help()
			elif guess == "c_word":
				screen.chosen_word(game.word)
			elif guess == "c_quit":
				if screen.confirm("Quit? [Y/n]: "):
					quit_flag = True
					break
		else:
			_is_correct = game.is_correct(guess)

			if len(guess) < 3:  # If user typed a word with less than 3 chars
				screen.short_word(3)
			elif _is_correct:  # If user is correct
				if _is_correct == "guessed":  #If already guessed
					screen.guessed()
				else:
					screen.correct()
					if gmode == "combine":
						screen.chosen_word(game.word)
			else:  # If user is wrong
				screen.retries(game.lives)

	if quit_flag:
		break

	# ------ POST GAME ------
	screen.calculate_score(game.score)

	if not screen.confirm("Play Again? [Y/n]: "):
		screen.on_exit()
		time.sleep(3)
		break

	screen.clear()



