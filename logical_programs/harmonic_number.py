
def harmonic_number(nth_number):
    """
    Prints harmonic number of given number
    :param nth_number: given max number
    :return: nothing
    """
    harmonic_num = 0

    if nth_number <= 0:
        print("Enter a value greater than 0")
        return

    for i in range(1, nth_number+1):
        harmonic_num = harmonic_num + (1/i)

    print(harmonic_num)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number greater than zero to find the nth harmonic number"))
        harmonic_number(number)
    except TypeError:
        print("Please enter valid value as mentioned above")

