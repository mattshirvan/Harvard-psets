from cs50 import get_int

# initialize a while to reprompt user for correct input
while True:

    # get heigt of pyramid
    n = get_int("Height: ")


    # check for proper height
    if n > 0 and n < 9:
        break


# draw pyramid
for index in range(n):
    for jenga in range(n - 1 - index):
        print(' ', end='')
    for jenga in range(index + 1):
        print('#', end='')
    print()