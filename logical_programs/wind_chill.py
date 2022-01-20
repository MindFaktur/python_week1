
def wind_chill(temperature, wind_speed):
    """
    Prints the wind chill value given temperature and wind speed
    :param temperature:
    :param wind_speed:
    :return:
    """

    if temperature <= 0 or temperature > 50 or wind_speed <= 3 or wind_speed > 120:
        print("Please enter correct values as mentioned above")
        return

    w = (35.74 + (0.6215 * temperature) + (0.4275 * temperature - 35.75) * (wind_speed ** 0.16))
    print("Wind chill is " + str(w))


if __name__ == "__main__":
    try:
        temp = float(input("Please enter the temperature(0 and 50) in farheneit : "))
        winds_peed = float(input("Please enter the speed(between 3 and 120) in miles per hour : "))
        wind_chill(temp, winds_peed)
    except TypeError:
        print("Please enter valid value as mentioned above")


