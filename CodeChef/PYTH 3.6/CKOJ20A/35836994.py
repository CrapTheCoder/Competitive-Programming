n = int(input())
a = sorted(map(int, input().split()))

j = -1

for i in range(n-2):
    if a[i] + a[i+1] > a[i+2]:
        j = i

if j == -1:
    print('NO')
else:
    print('YES')
    print(*[a[j], a[j+1], a[j+2]][::-1])