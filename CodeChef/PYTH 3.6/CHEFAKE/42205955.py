n = int(input())
s = input()

d = {i: 0 for i in range(n)}

for i in range(n):
    if s[i] != '1':
        continue

    for j in range(i, n):
        if s[j] == '1':
            d[j-i] += 1

print(*d.values())