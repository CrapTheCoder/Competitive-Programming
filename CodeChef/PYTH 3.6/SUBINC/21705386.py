for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [1] * n

    for i in range(1, n):
        if a[i - 1] <= a[i]:
            d[i] += d[i - 1]

    print(sum(d))