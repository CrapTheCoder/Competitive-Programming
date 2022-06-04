for _ in range(int(input())):
    n = int(input())

    maxi = 1

    m = 1
    while m < n:
        nm = min(n, m*2 - 1)

        maxi = max(maxi, nm - m + 1)
        m *= 2

    print(maxi)
