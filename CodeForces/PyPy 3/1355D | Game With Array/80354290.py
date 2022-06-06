n, s = map(int, input().split())
 
if n <= s // 2:
    print('YES')
    print(*[2] * (n-1) + [s - 2 * (n-1)])
    print(1)
 
else:
    print('NO')