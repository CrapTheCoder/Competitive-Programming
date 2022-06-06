for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    maxi = 0
 
    for i in range(1, n):
        if a[i] < a[i-1]:
            maxi = max(maxi, len(bin(a[i-1] - a[i])) - 2)
            a[i] = a[i-1]
 
    print(maxi)