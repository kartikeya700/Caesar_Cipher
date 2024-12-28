alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    from art import logo

    print(logo)

    # to run the cipher program while the user wants to continue
    restart = True
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while restart:
        # taking the user input
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text = text, shift_amount = shift, choice = direction)
        # asking if user wants to restart the cipher program or not
        choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        # to stop the loop in case of a negative response
        if choice == "no":
            restart = False
            print("Goodbye!")
        else:
            # to check if user wants to continue with previously entered direction or not
            direction_choice = input("Do you want to cotinue with same function type or change it? Type 'y' to continue else, type 'n'.").lower()
            if direction_choice == "n":
                direction = "decode"

def caesar(choice, original_text, shift_amount):
    output_text = ""
    # check for validity of the choice
    if choice != "decode" and choice != "encode":
        print("Please enter a valid option.")
        main()
    # to set shift amount to negative to reduce index in case of decoding
    elif choice == "decode":
        shift_amount *= -1

    for letter in original_text:
        # if the letter is not an alphabet then it is printed as such
        if letter not in alphabet:
            output_text += letter
        # for shifting the letter by req number and then appending it to the string
        else:
            new_index = alphabet.index(letter) + shift_amount
            # if index is less than 0 or greater than 25 then the index is adjusted to the other end of the alphabet
            if new_index > 25:
                new_index -= 26
            if new_index < 0:
                new_index += 26
            output_text += alphabet[new_index]
    print(f"Here is the {choice}d result: {output_text}")


if __name__ == '__main__':
    main()