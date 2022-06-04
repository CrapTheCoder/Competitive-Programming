for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    l, r = 0, n-1

    b = []

    for i in range(n):
        if i%2:
            b.append(a[l])
            l += 1
        else:
            b.append(a[r])
            r -= 1

    print(*b)