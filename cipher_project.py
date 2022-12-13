# New function created to define the cipher that takes the arguments
# word and shift
def cipher(_word: str, _shift: int):
    # ensures input is valid and improves testability
    if not _word.isalpha():
        raise Exception("Word contains non-alphabetical characters.")
    if _shift < 1 or _shift > 12:
        raise Exception("Shift must be between 1 and 12.")
    encryption = ""
    for letter in _word:
        # implements cipher shift
        code = ord(letter) + _shift
        # ensures letters remain within latin alphabet regardless of
        # upper/lowercase
        if (letter.isupper() and code > ord('Z')) or code > ord('z'):
            code -= 26
        # append encrypted letter to cipher string
        encryption += chr(code)
    return encryption


if __name__ == "__main__":
    # Asks user to input the word to be encrypted
    word = input("Enter your word: ")
    while not word.isalpha():
        print("Please enter a valid word.")
        word = input("Enter your word: ")
    # Sets shift based on birth month
    shift = int(input("Enter your birth month (01 - 12): "))
    # Ensures valid month is input
    while shift < 1 or shift > 12:
        print("Please input valid month.")
        shift = int(input("Enter your birth month (01 - 12): "))
    result = cipher(word, shift)
    # will ask user to input word made of alphabetical characters
    if result:
        print(result)
    else:
        print("Please enter a valid word.")
