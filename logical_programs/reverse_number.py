
def reverse_given_number(num):
    """
    Prints the reverse sequence of a number
    :param num: given number
    :return: nothing
    """
    print(num)
    remainder, reverse = 0, 0

    while num > 0:
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10

    print(reverse)


if __name__ == "__main__":
    try:
        number = int(input("Please enter a number to reverse it "))
        reverse_given_number(number)
    except TypeError:
        print("Please enter valid value as mentioned above")

