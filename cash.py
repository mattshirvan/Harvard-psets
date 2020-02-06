from cs50 import get_float

# create main function
def main():

    # prompt until proper input
    while True:

        # get change owed from user
        change = get_float("Change owed: ")

        # condition to break out of loop
        if change > 0:
            break

    # step counter
    coins = 0

    # convert change owed to integer
    change = int(change * 100)

    # loop over money to find amount of coins
    while change > 0:

        # take 25, 10, 5 and 1 as part of greedy algorithm
        if change >= 25:
            change -= 25
            coins += 1
        elif change >= 10 and change <  25:
            change -= 10
            coins += 1
        elif change >= 5 and change < 10:
            change -= 5
            coins += 1
        elif change >= 1 and change < 5:
            change -= 1
            coins += 1

    # print the amount of coins for greedy algorithm
    print(coins)

main()