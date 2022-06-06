from sys import stdin
 
input = stdin.readline
 
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
 
if n > m:
    print(0)
    exit()
 
f = 1
 
for i in range(n):
    for j in range(i):
        f = f * (a[i] - a[j]) % m
 
print(f)