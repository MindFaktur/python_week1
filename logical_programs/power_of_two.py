
def power_of_two(num):
    """
    Prints a table of 2 to the powers until it reaches the given 2^num value
    :param num: given max exponential
    :return: nothing
    """
    i = 0

    if num < 0 or num > 31:
        print("Please enter value as mentioned above")
        return

    while i <= num <= 31:
        print("2 power of " + str(i) + " is " + str(2 ** i))
        i += 1


if __name__ == "__main__":
    try:
        number = int(input("Enter the value between 0 to 31 to find the powers of 2 upto it: "))
        power_of_two(number)
    except TypeError:
        print("Please enter valid value as mentioned above")



