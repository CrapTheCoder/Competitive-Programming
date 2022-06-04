for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    maxi = float('-inf')

    for i in range(n):
        mini = float('inf')

        if i - 1 >= 0:
            mini = min(mini, abs(a[i] - a[i-1]))

        if i + 1 < n:
            mini = min(mini, abs(a[i+1] - a[i]))

        maxi = max(maxi, mini)

    print(maxi)