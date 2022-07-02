import random

from exceptions import NotSingleLetterException, NoSuchFormatException


def game():
    guessed_w = random.choice(words)
    hidden_w = "-" * len(guessed_w)
    guessed_letters = set()
    print("H A N G M A N")
    i = 0
    while i <= 8:
        print(f"\n{hidden_w}")
        print(i)
        letter = input("Input a letter:")
        try:
            check_ex(letter)
            if letter not in guessed_letters:
                guessed_letters.add(letter)
                if letter not in guessed_w:
                    print("That letter doesn't appear in the word.")
                    i += 1
                else:
                    hidden_w = "".join(j if j in guessed_letters else "-" for j in guessed_w)
            else:
                print("You've already guessed this letter.")
            if hidden_w == guessed_w:
                print(f"You guessed the word {hidden_w}!\nYou survived!")
                break
            if i == 8 and hidden_w != guessed_w:
                print("You lost!")
                break
        except (NoSuchFormatException, NotSingleLetterException) as ex:
            print(ex)


def check_ex(letter: str):
    if len(letter) > 1 or len(letter) < 1:
        raise NotSingleLetterException(letter)
    if not letter.isalpha() or letter.isupper():
        raise NoSuchFormatException(letter)


if __name__ == "__main__":
    words = ("python", "java", "swift", "javascript")
    game()
