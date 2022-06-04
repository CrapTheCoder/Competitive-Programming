for _ in range(int(input())):
    x, y = map(int, input().split())
    d = x // y

    l = []

    for i in range(1, 11):
        l.append(int(str(y * i)[-1]))

    print(sum(l) * (d // 10) + sum(l[:d%10]))
