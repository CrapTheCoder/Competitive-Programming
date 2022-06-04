def findTrailingZeroes(n):
    count = 0

    i = 5

    while True:
        d = n // i

        if d < 1:
            break

        count += d
        i *= 5

    return count

for _ in range(int(input())):
    print(findTrailingZeroes(int(input())))