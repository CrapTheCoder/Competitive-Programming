for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    maxi = max(a[i] - i for i in range(n))
 
    print(maxi-1)