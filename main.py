import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
raw_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(raw_data)
alphabet_code = {row.letter: row.code for (index, row) in raw_data.iterrows()}


# print(alphabet_code)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_alphabet():
    user_input = input("Enter a word: ").upper()

    # # exception handling using if-else:
    # digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # is_letter_exists = False
    # for letter in user_input:
    #     if letter in digits:
    #         is_letter_exists = True

    # if not is_letter_exists:
    #     user_result = [alphabet_code[letter] for letter in user_input]
    #     print(user_result)
    # else:
    #     print("You can enter only alphabets in the input..!")
    #     nato()

    # # exception handling using try-except-else
    try:
        user_result = [alphabet_code[letter] for letter in user_input]
    except KeyError:
        print("You can enter only alphabets in the input..!")
        nato_alphabet()  # recursion
    else:
        print(user_result)


nato_alphabet()
