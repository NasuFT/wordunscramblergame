commands = ['help', 'word', 'quit']  # Game Commands
gmodes = ['anagram', 'combine']  # Game Modes
gmodes_short = ['a', 'c']  # Game Modes (Short Keys)
modes = ['zen', 'timed', 'misery']  # Modes
modes_short = ['z', 't', 'm']  # Modes (Short Keys)


# Game Launch
ON_LAUNCH = "Hello! Welcome to the Autism Induced Word Unscrambler!\n"
# Select Game Mode
ON_SELECT_GMODE = """Select a Game Mode!
	Select the corresponding letter and press enter to start the game.

	> [A]nagram: What else is there!
	> [C]ombine: Unscramble the puzzle!
	> [H]olocaust: Coming out Winter 2018!
	"""
# Select Mode
ON_SELECT_MODE = """Select mode:
	Select the corresponding letter and press enter to start the game.\

	> [Z]en: 3 Lives Only.
	> [T]imed: 60 Seconds Only.
	> [M]isery: 3 Lives and 60 Seconds Only
	"""
# Anagram Game Mode Launch
ON_ANAGRAM_START = """Welcome to Search the Anagram!
	Try to find all anagrams of the given string.
	Only words of at least length 3 will be accepted

	E.g. "Stalin" -> "Sin", "Ail", "Ails", ...
	"""
# Combine Game Mode Launch
ON_COMBINE_START = """Welcome to Combine the Words!
	Try to find the shortest string that can be formed using the words shown.
	The string must be in alphabetical order.

	E.g. "Cahoots", "Slouch", "Lust" -> "Holocaust"
	"""
# Game Exit
ON_EXIT = "Thank you for playing Autism Induced Word Unscrambler!"


def ask(string, iterable):
	"""	Asks the user for valid input.
		The input is valid if it is found in the iterable.
	"""

	while(True):
		response = input(string).lower().rstrip()

		if response in iterable:
			return response
		else:
			print("Try Again.")

def confirm(string):
	"""	Prints string and returns True or False depending on user input.
		Only yes or no decisions are accepted.
	"""

	decision = ask(string, ('y', 'n', 'yes', 'no'))

	if decision in ('y', 'yes'):
		return True
	else:
		return False
		
def read_input(string = ""):
	"""	Reads player input and returns data accordingly.

		Also reads commands and returns "c_[command]" if needed.
		E.g. "/help" returns "c_help"
	"""

	while(True):
		_string = input(string).lower().rstrip()
		
		if _string != "":
			if _string[0] == "/":
				if _string[1:] in commands:
					return "c_{}".format(_string[1:])
				else:
					print("Unknown command!")
			else:
				return _string
		else:
			return _string
			
def start_game():
	"""	Prints text upon opening the game.
	"""

	print(ON_LAUNCH)

def select_gmode():
	"""	Prints text to select a game mode and returns the user input.
		Repeatedly prints text to try again if an invalid input is received.

		Only returns "anagram" or "combine" depending on game mode selected.
	"""

	print(ON_SELECT_GMODE)

	mode = ask("Choose Mode: ", gmodes + gmodes_short)
	
	if mode in gmodes:
		return gmodes[gmodes.index(mode)]
	else:
		return gmodes[gmodes_short.index(mode)]
	
def gmode_start(mode):
	"""	Prints introductory text according to game mode.
	"""

	if mode == "anagram":
		print(ON_ANAGRAM_START)
	elif mode == "combine":
		print(ON_COMBINE_START)
		
def select_mode():
	"""	Prints text to select a mode and returns the user input.
		Repeatedly prints text to try again if an invalid input is received.

		Only returns "zen", "timed", or "misery".
	"""

	print(ON_SELECT_MODE)

	mode = ask("Choose Mode: ", modes + modes_short)
	
	if mode in modes:
		return modes[modes.index(mode)]
	else:
		return modes[modes_short.index(mode)]

def short_word(length):
	"""	Prints text that the word is too short.
		The input needs to be of length of at least [length] letters.
	"""
	print("Words must have length of at least {} letters. Try again!".format(length))


def chosen_word(string):
	"""	Prints the chosen word.
	"""

	print("The word(s) is/are: {}".format(string))

def guessed():
	"""	Prints text that you have already guessed that word.
	"""

	print("You have already guessed that word. Try again!")

def calculate_score(num):
	"""	Prints your score over the game.
	"""

	print("""
Your score is {}.""".format(num))

def retries(n):
	""" Prints text to verify how many retries are left.
	"""

	print("Retries left: {}".format(n))

def correct():
	"""	Prints correct.
	"""

	print("Correct!")

def help():
	"""	Prints help text.
	"""

	string = "Commands: "

	for word in commands:
		string += "  /{}".format(word)

	print(string)

def on_exit():
	"""	Prints text when exiting the game.
	"""

	print(ON_EXIT)
	
