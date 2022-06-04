l = []

for _ in range(int(input())):
    l.append(list(map(int, input().split()))[:-1])

for i in sorted(l):
    print(*i)
