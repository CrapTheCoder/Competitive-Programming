from sys import stdin
 
input = stdin.readline
 
n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
i = j = 0
 
for i in range(n):
    if a[i] % p != 0:
        break
 
for j in range(m):
    if b[j] % p != 0:
        break
 
print(i + j)