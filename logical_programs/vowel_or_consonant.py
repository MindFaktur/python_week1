

def check_vowel_or_consonant(alphabet):
    """
    Prints if a given alphabet is a consonant or a vowel
    :param alphabet:
    :return:
    """
    if len(alphabet) > 1:
        print("Please enter a single alphabet")
        return

    alphabet = alphabet.lower()
    if alphabet in ("a", "e", "i", "o", "u"):
        print(alphabet + " is a vowel")
    else:
        print(alphabet + " is a consonant")


if __name__ == "__main__":
    try:
        alphabet_value = input("Enter an alphabet ")
        check_vowel_or_consonant(alphabet_value)
    except TypeError:
        print("Please enter valid value as mentioned above")



