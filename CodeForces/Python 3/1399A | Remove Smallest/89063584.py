for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    
    print('YES' if all(a[i] - a[i-1] <= 1 for i in range(1, n)) else 'NO')