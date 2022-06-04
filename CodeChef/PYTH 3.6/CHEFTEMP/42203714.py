a = list(map(int, input().split()))
f = list(map(int, input().split()))

s = 0

for i, j in zip(a, f):
    s += abs(i-j)

print(s)
