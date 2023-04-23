
import pandas

nato_code = pandas.read_csv("nato_phonetic_alphabet.csv")
code_received = False

nato_dict = {row.letter: row.code for (index, row) in nato_code.iterrows()}

while not code_received:
    word = input("Enter a word: ").upper()
    try:
        code_words = [nato_dict[item] for item in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(code_words)
        code_received = True
