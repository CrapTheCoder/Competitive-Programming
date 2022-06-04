n = int(input())
a = sorted([int(input()) for _ in range(n)])
b = a[::-1]

s1 = s2 = s3 = s4 = 0
for i in range(1, n // 2 + n%2):
    s1 += abs(a[i] - b[i-1])

for i in range(n // 2 + n%2, n-1):
    s2 += abs(a[i] - b[i+1])

for i in range(1, n // 2 + n%2):
    s3 += abs(b[i] - a[i-1])

for i in range(n // 2 + n%2, n-1):
    s4 += abs(b[i] - a[i+1])

# print(s1, s2)
# print(s3, s4)

print(max(s1 + s2, s3 + s4) + abs(a[0] - b[0]))