
def swap_numbers(d, e):
    """
    Swaps the given numbers
    :param d:
    :param e:
    :return:
    """
    a, b = d, e
    print(" a : " + str(a) + " b : " + str(b))

    c = a
    a, b = b, c
    print(" a : " + str(a) + " b : " + str(b))


if __name__ == "__main__":
    try:
        number_a = int(input("Enter the number a "))
        number_b = int(input("Enter the number b "))
        swap_numbers(number_a, number_b)
    except TypeError:
        print("Please enter valid value as mentioned above")





