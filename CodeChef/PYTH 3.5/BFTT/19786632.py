for _ in range(int(input())):
    n = int(input())
    a = n + 1

    while str(a).count('3') < 3:
        a += 1

    print(a)
