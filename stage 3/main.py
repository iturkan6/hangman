import random

words = ("python", "java", "swift", "javascript")
print("H A N G M A N")
given_word = input("Guess the word:")
guessed_word = random.choice(words)
print("You survived!" if given_word.lower() == guessed_word else "You lost!")
