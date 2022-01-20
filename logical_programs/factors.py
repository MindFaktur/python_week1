import math


def prime_factorization(num):
    """
    Prints factors of a number
    :param num: number whose prime factors are to be printed
    :return: nothing
    """
    while num % 2 == 0:
        print(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num) + 1), 2):
        if num % i == 0:
            print(i)
            num = num / i

    if num > 2:
        print(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number to find its prime factors : "))
        prime_factorization(number)
    except TypeError:
        print("Please enter valid value as mentioned above")

