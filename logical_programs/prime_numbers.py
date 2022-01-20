
def prime_numbers(num):
    """
    Prints the list of prime numbers until the given value
    :param num: max number
    :return: nothing
    """

    list_of_prime_numbers = [1, 2, ]
    i = 3

    for i in range(i, num):
        decision = 0
        for j in range(2, i):
            if i % j == 0:
                decision = 1
                break
        if decision == 0:
            list_of_prime_numbers.append(i)

    print(list_of_prime_numbers)


if __name__ == "__main__":
    try:
        number = int(input("Please enter a number to find prime numbers upto it "))
        prime_numbers(number)
    except TypeError:
        print("Please enter valid value as mentioned above")

