
def even_or_odd(num):
    """
    Prints if a given number is odd or even
    :param num: given number by user
    :return: nothing
    """
    if num % 2 == 0:
        print(str(num) + " is a even number")
    else:
        print(str(num) + " is a odd number")


if __name__ == "__main__":
    try:
        number = int(input("Please enter a number to check if its even or odd: "))
        even_or_odd(number)
    except TypeError:
        print("Please enter valid value as mentioned above")
