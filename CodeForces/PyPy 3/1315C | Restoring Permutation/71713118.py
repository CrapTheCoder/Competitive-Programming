from bisect import bisect_right

for _ in range(int(input())):
n = int(input())
b = list(map(int, input().split()))

try:
a = [0] * 2 * n
a[::2] = b.copy()

m = sorted(set(range(1, 2 * n + 1)).difference(set(b))) + [float('inf')]

for i in range(1, 2 * n, 2):
a[i] = m.pop(bisect_right(m, a[i-1]))

if list(range(1, 2 * n + 1)) != sorted(a):
print(-1)
else:
print(*a)

except:
print(-1)