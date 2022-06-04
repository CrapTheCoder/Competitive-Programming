for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(*([a[0] & a[1]] + [max((a[i] & a[i-1]), (a[i+1] & a[i])) for i in range(1, n-1)] + [a[-1] & a[-2]]))