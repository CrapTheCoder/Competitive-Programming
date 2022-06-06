from sys import stdin
input = stdin.readline

for _ in range(int(input())):
input()

c = ans = 0

for i in sorted(map(int, input().split())):
c += 1

if c >= i:
ans += 1
c = 0

print(ans)