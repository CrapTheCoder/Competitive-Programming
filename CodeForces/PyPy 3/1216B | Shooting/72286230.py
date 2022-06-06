n = int(input())
a = list(map(int, input().split()))

l = sorted(zip(a, range(1, n + 1)), reverse=True)

c = 0

for i in range(n):
c += l[i][0] * i + 1

print(c)
print(*(i[1] for i in l))