from cs50 import get_int


while True:
    n = get_int("Height: ")

    if n > 0 or n < 9:
        break

for i in range(n):
    for j in range(n - 1 -i):
        print(' ', end='')
    for j in range(i + 1):
        print('#', end='')
    print()