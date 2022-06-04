for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    s = 0

    for i in range(n // 2):
        s += abs(a[i] - a[n-1-i])

    print(s)