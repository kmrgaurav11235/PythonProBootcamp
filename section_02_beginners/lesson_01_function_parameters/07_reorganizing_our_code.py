alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift_amount, cipher_direction):
    result_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = 0
        if cipher_direction == "encode":
            new_position = (position + shift_amount) % len(alphabet)
        elif cipher_direction == "decode":
            new_position = position - shift_amount
        else:
            print("Invalid input. Allowed values: encode, decode")
            exit(0)
        result_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {result_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift_amount=shift, cipher_direction=direction)
