import math


def distance_of_point_from_origin(first, second):
    """
    This prints the distance between origin and given point
    :param first: x point
    :param second: y point
    :return: nothing
    """
    x = first
    y = second
    point = (x, y)
    print("the distance of point" + str(point) + " from origin is " + str(math.sqrt(x ** x + y ** y)))


if __name__ == "__main__":
    try:
        distance_of_point_from_origin(int(input("Enter x value: ")), int(input("Enter y value: ")))
    except TypeError:
        print("Please enter valid value as mentioned above")
