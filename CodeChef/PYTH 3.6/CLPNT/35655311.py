from bisect import bisect_left as bisect

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for _ in range(int(input())):
        x, y = map(int, input().split())

        m = x + y

        i = bisect(a, m)

        if i < n and a[i] == m:
            print(-1)
        else:
            print(i)