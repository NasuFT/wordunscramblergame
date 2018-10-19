import engine
import interface
import random

dictionary = engine.read_file("dictionary.txt")

interface.start_game()
mode = interface.choose_mode()

if mode == "anagram":
	interface.anagram_start()
elif mode == "combine":
	pass