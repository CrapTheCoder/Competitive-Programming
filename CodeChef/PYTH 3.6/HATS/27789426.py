l = [1, 1, 2, 1, 3, 2, 3, 2, 3]

for _ in range(int(input())):
    n = int(input())

    if n <= 9:
        y = l[n - 1]
    else:
        if n % 2:
            y = int(n ** 0.5) + 1 - (n ** 0.5).is_integer()
        else:
            y = int(n ** 0.5) - (n ** 0.5).is_integer()

    print(y)
