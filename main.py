import pandas

# # concept code
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
raw_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(raw_data)
alphabet_code = {row.letter: row.code for (index, row) in raw_data.iterrows()}
# print(alphabet_code)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_result = [alphabet_code[letter] for letter in user_input if letter in alphabet_code]
print(user_result)
