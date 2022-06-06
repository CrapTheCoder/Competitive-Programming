for _ in range(int(input())):
n = int(input())
c = n // 2, n // 2

s = 0

for j in range(n):
s += max(abs(c[0] - 0), abs(c[1] - j))

ts = s

for i in range(1, n // 2 + 1):
s -= n - 2 * i
ts += s

print(ts * 2 - s)