
def print_fibonacci_numbers(num):
    """
    Prints fibonacci series till it reaches a given number
    :param num: max series number
    :return: nothing
    """
    a, b = 0, 1
    print(a, end=",")
    while b <= num:
        print(b, end=",")
        c = a + b
        a, b = b, c


if __name__ == "__main__":
    try:
        number = int(input("Enter a number to print fibonacci numbers: "))
        print_fibonacci_numbers(number)
    except TypeError:
        print("Please enter valid value as mentioned above")