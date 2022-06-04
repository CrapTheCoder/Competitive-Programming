for _ in range(int(input())):
    n = int(input())
    a = [float('inf')] + list(map(int, input().split()))
    c = 0

    for i in range(1, n+1):
        if min(a[max(0, i-5):i]) > a[i]:
            c += 1

    print(c)
