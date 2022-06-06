for _ in range(int(input())):
    n = int(input())
 
    a = sorted(map(int, input().split()))
 
    print(a[n] - a[n - 1])