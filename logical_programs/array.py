

def array_2d():
    """
    Takes in values and inputes them into the arrays
    :return: Nothing is returned but the values are printed
    """
    cols = int(input("Enter the number of columns: "))
    rows = int(input("Enter the number of rows: "))

    array_example = []

    for i in range(0, rows):
        inner_array = []
        for j in range(0, cols):
            inner_array.append(int(input("Enter array value of a[" + str(i) + "," + str(j) + "]: ")))
        array_example.append(inner_array)

    print(array_example)


if __name__ == "__main__":
    array_2d()

