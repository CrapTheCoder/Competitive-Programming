n = int(input())
p = list(map(int, input().split()))

lis = []

i = n

while i != 1:
lis.append(i)
i = p[i - 2]

print(*[1] + lis[::-1])