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

def start_game():
	"""	Prints text upon opening the game.
	"""

	print("Hello! Welcome to the Autism Induced Word Unscrambler!\n")

def short_word(length):
	"""	Prints text that the word is too short.
		The input needs to be of length of at least [length] letters.
	"""
	print("Words must have length of at least {} letters. Try again!".format(length))

def select_gmode():
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

	mode = ask("Choose Mode: ", ("a", "c", "anagram", "combine"))
	
	if mode in ("a", "anagram"):
		return "anagram"
	elif mode in ("c","combine"):
		return "combine"
	
def anagram_start():
	""" Prints introductory text when choosing Anagram Game Mode.
	"""

	print("""
Welcome to Search the Anagram!
	Try to find all anagrams of the given string.
	Only words of at least length 3 will be accepted

	E.g. "Stalin" -> "Sin", "Ail", "Ails", ...
		""")

def chosen_word(string):
	"""	Prints the chosen word.
	"""

	print("The word(s) is/are: {}".format(string))

def guessed():
	"""	Prints text that you have already guessed that word.
	"""

	print("You have already guessed that word. Try again!")

def calculate_score(num):
	"""	Prints your score over the game
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

def combine_start():
	"""	Prints introductory text when choosing Combine Game Mode.
	"""

	print("""
Welcome to Combine the Words!
	Try to find the shortest string that can be formed using the words shown.
	The string must be in alphabetical order.

	E.g. "Cahoots", "Slouch", "Lust" -> "Holocaust"
		""")

def select_mode():
	"""	Prints text to select a mode and returns the user input.
		Repeatedly prints text to try again if an invalid input is received.

		Only returns "zen", "timed", or "misery".
	"""

	print("""
Select mode:
	Select the corresponding letter and press enter to start the game.\

	> [Z]en: 3 Lives Only.
	> [T]imed: 60 Seconds Only.
	> [M]isery: 3 Lives and 60 Seconds Only
		""")

	mode = ask("Choose Mode: ", ("z", "t", "c", "m", "zen", "timed", "misery", "cancel"))
	
	if mode in ("z", "zen"):
		return "zen"
	elif mode in ("t", "timed"):
		return "timed"
	elif mode in ("m", "misery"):
		return "misery"
	elif mode in ("c", "cancel"):
		return "cancel"

def game_confirm():
	"""	Prints text to confirm start of game.
	"""

	decision = ask("START GAME? [Y/n]: ", ("y", "n", "yes", "no"))

	if decision in ("y", "yes"):
		return True
	elif decision in ("n", "no"):
		return False

def play_again():
	"""	Asks if the user wants to play again.
	"""

	decision = ask("Play Again? [Y/n]: ", ("y", "n", "yes", "no"))

	if decision in ("y", "yes"):
		return True
	elif decision in ("n", "no"):
		return False

def read_input():
	"""	Reads player input and returns data accordingly.

		Also reads commands and returns "c_[command]" if needed.
		E.g. "/help" returns "c_help"
	"""

	while(True):
		string = input().lower().rstrip()
		
		if len(string) < 1:
			short_word(1)
		elif string[0] == "/":
			string = string[1:]

			if string == "help":
				return "c_help"
			elif string == "word":
				return "c_word"
			else:
				print("Unknown command!")
		else:
			return string

def help():
	"""	Prints help text
	"""

	print("Commands: /help, /word")

def on_exit():
	"""	Prints text when exiting the game.
	"""

	print("Thank you for playing Autism Induced Word Unscrambler!")
	
