import math


def quadratic(a, b, c):
    """
    Prints the root of a quadratic equation
    :param a:
    :param b:
    :param c:
    :return: nothing
    """
    print(" The quadratic equation is (" + str(a) + "x^2 + " + str(b) + "x + " + str(c) + ")")

    delta = (b * b - (4 * a * c))
    x1 = (-b + (math.sqrt(math.fabs(delta)) / (2 * a)))
    x2 = (-b - (math.sqrt(math.fabs(delta)) / (2 * a)))

    print(" Root 1 of x is " + str(x1))
    print(" Root 2 of x is " + str(x2))


if __name__ == "__main__":
    try:
        number1 = int(input("enter value of a "))
        number2 = int(input("enter value of b "))
        number3 = int(input("enter value of c "))
        quadratic(number1, number2, number3)
    except TypeError:
        print("Please enter valid value as mentioned above")
