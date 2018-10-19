def start_game():
	"""	Prints text upon opening the game.
	"""

	print("Hello! Welcome to the Autism Induced Word Unscrambler!\n")

def choose_mode():
	"""	Prints text to select a game mode and returns the user input.
		Repeatedly prints text to try again if an invalid input is received.

		Only returns "anagram" or "combine" depending on game mode selected.
	"""

	print("""Select a Game Mode!
	Select the corresponding letter and press enter to start the game.

	> [A]nagram: What else is there!
	> [C]ombine: Unscramble the puzzle!
	> [H]olocaust: Coming out Winter 2018!
		""")

	while(True):
		mode = input("Choose Mode: ").lower()

		if mode in ("a", "c", "anagram", "combine"):
			break
		else:
			print("Try Again.")

	if mode in "anagram":
		return "anagram"
	elif mode in "combine":
		return "combine"
	
def anagram_start():
	""" Prints introductory text when choosing Anagram Game Mode.
	"""

	print("""
Welcome to Search the Anagram!
	Try to find all anagrams of the given string.
	You are only given 3 mistakes before game over is called.

	E.g. "Stalin" -> "Sin", "Ail", "Ails", ...
		""")

def retries(n):
	""" Prints text to verify how many retries are left.
	"""

	print("Retries left: {}".format(n))


if __name__ == "__main__":
	pass