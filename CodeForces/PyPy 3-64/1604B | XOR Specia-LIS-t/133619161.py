for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if n % 2 == 0:
        print('YES')
        continue
 
    if all(a[i] < a[i+1] for i in range(n-1)):
        print('NO')
    else:
        print('YES')