import random


def coin_flip(num_times_to_flip):
    """
    Flips the coin 'n' number of times given by the user
    :return: returns nothing
    """

    times_flipped = 0
    total_heads = 0
    total_tails = 0

    if num_times_to_flip <= 0:
        print("please enter a value above 0 ")
        return

    while times_flipped < num_times_to_flip:
        choice = random.randrange(0, 2)
        if choice == 0:
            total_tails += 1
            times_flipped += 1
        else:
            total_heads += 1
            times_flipped += 1

    print("No of times coin flipped is " + str(times_flipped))
    print("No of times head occurred " + str(total_heads) + " percentage is " +
          str(total_heads * 100/num_times_to_flip))
    print("No of times tails occurred " + str(total_tails) + " percentage is " +
          str(total_tails * 100/num_times_to_flip))


if __name__ == "__main__":
    try:
        num_times = int(input("Please enter the number of times to flip the coin: "))
        coin_flip(num_times)
    except TypeError:
        print("Please enter valid value as mentioned above")




