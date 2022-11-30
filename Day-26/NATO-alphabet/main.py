import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_not_valid = True
while is_not_valid:
    word = input("Enter a word: ").upper()
    try:
        result = [data_dict[letter] for letter in word]
    except KeyError as error:
        print(f"{error} is an invalid character. Please enter only letters.")
    else:
        print(result)
        is_not_valid = False

