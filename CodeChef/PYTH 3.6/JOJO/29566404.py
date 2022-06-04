for _ in range(int(input())):
    n = input().strip().lstrip('0')

    x = sum(int(i) for i in n) % 10

    if x == 0:
        x = 10

    print(str(n) + str(10 - x))
