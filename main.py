import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
raw_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(raw_data)
alphabet_code = {row.letter: row.code for (index, row) in raw_data.iterrows()}
# print(alphabet_code)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_result = [alphabet_code[letter] for letter in user_input if letter in alphabet_code]
print(user_result)
