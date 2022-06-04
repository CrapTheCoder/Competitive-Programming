for _ in range(int(input())):
    n = list(map(int, input().strip()))

    while n and (n[-1] % 2 == 0):
        n.pop()

    s = sum(i for i in n)

    if not n:
        print(-1)
        continue

    if s % 2 == 0:
        print(0)
        continue

    for i in range(len(n) - 1):
        if (s - n[i]) % 2 == 0:
            print(1)
            break
    else:
        print(-1)
        continue
