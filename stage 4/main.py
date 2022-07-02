import random

words = ("python", "java", "swift", "javascript")
print("H A N G M A N")
guessed_word = random.choice(words)
given_word = input(f"Guess the word {guessed_word[0:3]}" + "-"*(len(guessed_word)-3) + ":")

print("You survived!" if given_word.lower() == guessed_word else "You lost!")
