n = int(input())
a = set(map(int, input().split()))

c = 0

for i in a:
    if i % 5 and i % 2 == i % 3 == 0:
        c += 1

print(c)