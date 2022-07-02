class NotSingleLetterException(Exception):
    def __init__(self, letter):
        self.letter = letter

    def __str__(self):
        return "Please, input a single letter."


class NoSuchFormatException(Exception):
    def __init__(self, letter):
        self.letter = letter

    def __str__(self):
        return "Please, enter a lowercase letter from the English alphabet."