# Readme
1. Download and install Python 3.7.0 or later from https://www.python.org/downloads/

2. Run Command Prompt and change directory to root folder

3. Type the following commands:
```
cd scripts
activate
cd ..
python main.py
```

4. To deactivate, navigate to root folder and type:
```
cd scripts
deactivate
```

# Important Notes: Game Modes
Game Modes have to accept 2 parameters, the dictionary file and the usage of screen.
```
dictionary = engine.read_file('dictionary.txt')
screen = interface.Terminal()
game = engine.AnagramMode(dictionary, screen)
```
Game Modes have 3 important methods:
```
game.is_correct()
game.has_guessed()
game.is_alive()
```
# Important Notes: Interfaces
Interfaces must have the following methods:
```
screen.clear()
word = screen.read_input()
screen.confirm()
screen.start_game()
mode = screen.select_mode()
screen.mode_start(mode)
screen.chosen_word(game.word)
screen.help()
screen.has_guessed()
screen.on_correct(game.score)
screen.on_mistake(game.lives)
screen.calculate_score()
screen.on_exit()
```
It doesn't matter if any of this do nothing as long as these methods exist.


# Defaults
Anagram Mode:
```
min_length = 6
max_length = 15
lives = 3
```
Combine Mode:
```
min_size = 3
max_size = 6
lives = 3
```


# Autism Induced Word Unscrambler

Congratulations! You are now autistic.

Please play this word unscrambler to decide your fate.

# Conditions

If you win, you get 2500 V-Bucks.

If you lose, your citizenship will be converted to Russian.

If you win but also lose at the same time,
The Chancellor of the German Reich shall be reborn.