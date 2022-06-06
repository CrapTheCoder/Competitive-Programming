for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    res = [a[0]] if n % 2 else []
 
    for i in range(n % 2, n-1, 2):
        if a[i] < a[i+1]:
            res.append(a[i])
            res.append(a[i+1])
        else:
            res.append(a[i+1])
            res.append(a[i])
 
    if res == sorted(res):
        print('YES')
    else:
        print('NO')