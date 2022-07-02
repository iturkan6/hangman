import random
import re


def game(words):
    guessed_word = random.choice(words)
    string = list("-" * len(guessed_word))
    print("H A N G M A N\n")
    for _ in range(8):
        print(*string, sep="")
        letter = input("Input a letter:")
        result = put_letters(string, guessed_word, letter)
        if not result:
            print("That letter doesn't appear in the word.")
        else:
            string = result
    print("Thanks for playing!")


def put_letters(string, guessed_word, letter):
    indexes = [i.start() for i in re.finditer(letter, guessed_word)]
    if letter not in guessed_word:
        return False
    for i in indexes:
        string[i] = letter
    return string


def main():
    game(data)


if __name__ == "__main__":
    data = ("python", "java", "swift", "javascript")
    main()
