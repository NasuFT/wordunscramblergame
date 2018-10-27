# Important Notes: Game Modes
Game Modes have to accept 2 parameters, the dictionary file and the usage of screen.
```
dictionary = engine.read_file('dictionary.txt')
screen = interface.Terminal()
game = engine.AnagramMode(screen)
```
Game Modes have 2 important methods:
```
game.is_correct()
game.is_alive()
```
# Important Notes: Interfaces
Interfaces must have the following methods:
```
screen.clear()
screen.read_input()
screen.confirm()
screen.start_game()
screen.select_gmode()
screen.gmode_start(gmode)
screen.chosen_word()
screen.help()
screen.short_word()
screen.guessed()
screen.correct()
screen.retries()
screen.calculate_score()
screen.on_exit()
```
It doesn't matter if any of this do nothing as long as these methods exist.


# Defaults:
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
min_length = 4
max_length = 7
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