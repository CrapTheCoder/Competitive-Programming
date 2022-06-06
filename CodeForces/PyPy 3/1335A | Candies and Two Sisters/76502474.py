for _ in range(int(input())):
n = int(input())

if n % 2 == 0:
a, b = n // 2 - 1,  n // 2 + 1
else:
a, b = n // 2 + 1, n // 2

if n % 2 == 0:
print(min(a, n - b))
else:
print(min(a, n - b) - 1)