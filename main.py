import engine
import interface
import random
import time

dictionary = engine.read_file("dictionary.txt")

while(True):
	# BEFORE THE GAME STARTS

	interface.start_game()
	gmode = interface.select_gmode()

	if gmode == "anagram":
		interface.anagram_start()
	elif gmode == "combine":
		interface.combine_start()

	mode = interface.select_mode()
	if mode == "cancel":
		continue
	
	if not interface.game_confirm():
		continue

	seed = input("Enter seed (Leave blank if unsure): ").rstrip()
	if seed != "":
		random.seed(seed)
	
	# DURING THE GAME

	if gmode == "anagram":
		pass
	elif gmode == "combine":
		pass

	# AFTER THE GAME

	if not interface.play_again():
		break
