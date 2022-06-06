n, k = list(map(int, input().split()))

o = s = input()
s = s[:k]

d1 = (s * (n // k + 1))[:n]
d2 = (str(int(s) + 1) * (n // k + 1))[:n]

print(n)

if d1 >= o:
print(d1)
else:
print(d2)