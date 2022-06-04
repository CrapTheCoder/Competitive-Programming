for _ in range(int(input())):
    n = int(input())

    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    c = 0

    for i in range(1, n + 1):
        if a[i] - a[i-1] < b[i]:
            c += 1

    print(n - c)