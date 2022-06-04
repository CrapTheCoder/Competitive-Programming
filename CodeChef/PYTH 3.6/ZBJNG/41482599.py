from sys import stdin
input = stdin.readline

n = int(input())
s = set()

r = {}

for _ in range(n):
    a, b = map(int, input().split())
    r[a] = b

for a, b in r.items():
    if (a+b in r) and (a+b + r[a+b] == a):
        print('YES')
        break
else:
    print('NO')
