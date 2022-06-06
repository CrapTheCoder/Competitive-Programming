for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if a[0] + a[1] > a[-1]:
        print(-1)
    else:
        print(1, 2, n)