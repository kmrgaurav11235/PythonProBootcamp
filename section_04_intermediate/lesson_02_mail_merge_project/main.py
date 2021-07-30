STARTING_LETTER_FILE_PATH = "Input/Letters/starting_letter.txt"
INVITED_NAMES_FILE_PATH = "Input/Names/invited_names.txt"
READY_TO_SEND_FOLDER_PATH = "Output/ReadyToSend/"
NAME_PLACEHOLDER = "[name]"

# Create a letter using starting_letter.txt
with open(file=STARTING_LETTER_FILE_PATH, mode="r") as starting_letter_file:
    letter_text = starting_letter_file.read()

# for each name in invited_names.txt
with open(file=INVITED_NAMES_FILE_PATH, mode="r") as invited_names_file:
    invited_names_list = invited_names_file.readlines()

for name in invited_names_list:
    name_without_whitespace = name.strip()

    # Replace the [name] placeholder with the actual name.
    new_letter = letter_text.replace(NAME_PLACEHOLDER, name_without_whitespace)
    new_letter_file_path = f"{READY_TO_SEND_FOLDER_PATH}Letter_For_{name_without_whitespace}.txt"

    # Save the letters in the folder "ReadyToSend".
    with open(file=new_letter_file_path, mode="w") as new_letter_file:
        new_letter_file.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp
