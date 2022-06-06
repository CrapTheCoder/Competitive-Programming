for _ in range(int(input())):
n, m = map(int, input().split())

l = []

for i in range(1, 11):
l.append(int(str(m * i)[-1]))

print(sum(l) * ((n // m) // 10) + sum(l[:(n // m) % 10]))