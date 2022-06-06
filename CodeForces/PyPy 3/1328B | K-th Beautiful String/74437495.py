for _ in range(int(input())):
n, k = map(int, input().split())
x = n * (n - 1) // 2

c = n-1

while x - c >= k:
x -= c
c -= 1

l = ['a'] * n
l[c] = 'b'
l[c+(k-x-1)] = 'b'

print(*l[::-1], sep='')