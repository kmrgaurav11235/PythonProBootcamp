import pandas

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_ph_alphabet_data_frame = pandas.read_csv("04_nato_phonetic_alphabet.csv")
nato_ph_alphabet_dict = {row.letter: row.code for (index, row) in nato_ph_alphabet_data_frame.iterrows()}
# print(nato_ph_alphabet_dict)

is_input_valid = False

while not is_input_valid:
    try:
        # 2. Create a list of the phonetic code words from a word that the user inputs.
        input_word = input("Enter your word: ").upper()
        output_list = [nato_ph_alphabet_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        is_input_valid = True
