l = []

for i in range(int(input())):
    l.append(int(input()))

print(*sorted(l), sep='\n')