a, b = 0, 1
n = int(input())

for _ in range(n):
    a, b = b, (a + b) % 15746

print(b)
