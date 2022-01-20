

def sum_of_three(num_of_integers):
    """
    prints 3 integers from a given list if the sum is equal to zero
    :param num_of_integers: number of integers the user will enter
    :return: nothing
    """
    entered_integers = []

    for i in range(0, num_of_integers):
        entered_integers.append(int(input("enter integer: ")))
    print(entered_integers)

    for i in range(0, len(entered_integers)):
        for j in range(i+1, len(entered_integers)):
            for k in range(j+1, len(entered_integers)):
                if entered_integers[i] + entered_integers[j] + entered_integers[k] == 0:
                    print(str(entered_integers[i]) + " + " + str(entered_integers[j]) + " + " +
                          str(entered_integers[k]) + " is 0 ")


if __name__ == "__main__":
    try:
        number_of_int = int(input("Enter the number of integers you will enter: "))
        sum_of_three(number_of_int)
    except TypeError:
        print("Please enter valid value as mentioned above")


