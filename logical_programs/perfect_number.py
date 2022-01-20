
def perfect_number(num):
    """
    Prints if a given number if perfect number(All its divisors add upto it)
    :param num: user given number
    :return: nothing
    """
    i = 1
    total = 0
    list_of_divisors = []
    while i < num:
        if num % i == 0:
            list_of_divisors.append(i)
            total = total + i
        i = i + 1

    if total == num:
        print(str(num) + " is a perfect number and its divisors are ")
        print(list_of_divisors)
    else:
        print(str(num) + " is not a perfect number")


if __name__ == "__main__":
    try:
        number = int(input("Please enter the number to find if its a perfect number: "))
        perfect_number(number)
    except TypeError:
        print("Please enter valid value as mentioned above")
