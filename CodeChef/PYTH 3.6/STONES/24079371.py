for _ in range(int(input())):
    j = set(input())
    s = input()

    c = 0

    for i in j:
        c += s.count(i)

    print(c)