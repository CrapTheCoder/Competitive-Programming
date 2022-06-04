for  _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    l = [set(a[i: i + n // 4]) for i in range(0, n, n // 4)]

    for i in range(1, 4):
        if l[i-1].intersection(l[i]):
            print(-1)
            break
    else:
        print(*(min(i) for i in l[1:]))
