

def largest_among_three_numbers(first_num, second_num, third_num):
    """
    Prints largest of given three numbers
    :param first_num: 1st number
    :param second_num: 2nd number
    :param third_num: 3rd number
    :return: nothing
    """
    largest_num = first_num

    if third_num < second_num > first_num:
        largest_num = second_num
    elif third_num > first_num:
        largest_num = third_num

    print(largest_num)


if __name__ == "__main__":
    try:
        first_number = int(input("enter first number: "))
        second_number = int(input("enter second number: "))
        third_number = int(input("enter third number: "))
        largest_among_three_numbers(first_number, second_number, third_number)
    except TypeError:
        print("Please enter valid value as mentioned above")


