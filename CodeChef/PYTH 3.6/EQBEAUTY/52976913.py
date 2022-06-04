for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    if n == 2:
        print(0)
        continue

    if n == 3:
        print(min(a[2] - a[1], a[1] - a[0]))
        continue

    l = 1
    r = n-2

    mini = float('inf')

    mini = min(mini, sum(abs(a[i] - a[n // 2 - 1]) for i in range(n-1)))
    mini = min(mini, sum(abs(a[i] - a[n // 2]) for i in range(1, n)))

    while l < r:
        mini = min(mini, abs((a[0] + a[-1]) - (a[l] + a[r])))

        if a[l] + a[r] > a[0] + a[-1]:
            r -= 1
        else:
            l += 1

    print(mini)
