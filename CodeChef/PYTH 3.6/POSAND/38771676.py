for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n & (n-1) == 0:
        print(-1)
        continue

    a = [2, 3, 1]
    av = list(range(4, n+1))[::-1]

    for i in range(4, n+1):
        if i & (i-1) == 0:
            a.append(av.pop(-2))
        else:
            a.append(av.pop())

    print(*a)
