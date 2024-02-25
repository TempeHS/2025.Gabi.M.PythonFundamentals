# make function to remove vowels
def remove_vowels(text):
    # set list of vowels ommitable
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    no_vowels = " "
    for c in text:
        if c not in vowels:
            no_vowels += c
    return no_vowels


# ask user for input
def main():
    text = input("Enter text: ")
    text_no_vowels = remove_vowels(text)
    print(text_no_vowels)


main()
