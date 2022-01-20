
def leap_year(year):
    """
    Prints if a given year is a leap year or no
    :param year: 4 digit year
    :return: nothing
    """

    if year < 999 or year > 10000:
        print("please enter a 4 digit year")
        return
    else:
        if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
            print(str(year) + " is a leap year ")
        else:
            print(str(year) + " is not a leap year ")


if __name__ == "__main__":
    try:
        year_number = int(input("please enter the year to check if its a leap year: "))
        leap_year(year_number)
    except TypeError:
        print("Please enter valid value as mentioned above")
