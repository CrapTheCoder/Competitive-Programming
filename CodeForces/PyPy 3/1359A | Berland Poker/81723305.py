for _ in range(int(input())):
n, m, k = map(int, input().split())
x = n // k

if x >= m:
print(m)
continue

print(x - -(-(m - x) // (k - 1)))