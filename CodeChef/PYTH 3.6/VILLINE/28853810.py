n = int(input())
a, b = map(int, input().split())

s1 = s2 = 0

for _ in range(n):
    x, y, p = map(int, input().split())

    if y > a * x + b:
        s1 += p
    else:
        s2 += p

print(max(s1, s2))