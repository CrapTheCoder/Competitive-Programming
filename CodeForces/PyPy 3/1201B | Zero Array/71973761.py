n = int(input())
a = sorted(map(int, input().split()))
 
if sum(a) % 2 or sum(a[:-1]) < a[-1]:
    print('NO')
    exit()
 
print('YES')