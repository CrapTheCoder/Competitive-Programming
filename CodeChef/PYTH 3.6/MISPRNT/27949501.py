for _ in range(int(input())):
    n = int(input())
    v = input().split()

    c = 0

    s = input()

    for i in s:
        if i in v:
            c += 1

    print(c)