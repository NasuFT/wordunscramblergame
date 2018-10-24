import engine
import interface

dictionary = engine.read_file("dictionary.txt")

while True:
	interface.start_game()
	gmode = interface.select_gmode()  # Select Game Mode
	mode = interface.select_mode()  # Select Mode

	if not interface.game_confirm():  # Game Start Confirmation
		continue



	if gmode == "anagram":
		root = engine.AnagramMode(dictionary, mode)
	else:
		pass

