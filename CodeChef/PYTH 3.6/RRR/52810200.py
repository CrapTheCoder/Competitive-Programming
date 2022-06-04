for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = -1
    if k == 1:
        ans = n-1
    else:
        ans = n - (k // 2) - 1

    print(ans * 2)