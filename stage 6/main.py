import random


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
        if letter not in guessed_letters:
            guessed_letters.add(letter)
            if letter not in guessed_w:
                print("That letter doesn't appear in the word.")
                i += 1
            else:
                hidden_w = "".join(j if j in guessed_letters else "-" for j in guessed_w)
        else:
            print("No improvements.")
            i += 1
        if hidden_w == guessed_w:
            print(f"{hidden_w}\nYou guessed the word!\nYou survived!")
            break
        if i == 8 and hidden_w != guessed_w:
            print("You lost!")
            break


if __name__ == "__main__":
    words = ("python", "java", "swift", "javascript")
    game()
