from string import punctuation

l = []

for _ in range(int(input())):
    s = input().lower()

    for i in punctuation:
        s = s.replace(i, '')

    l.extend(s.split())

l = sorted(set(l))

print(len(l))
print(*l, sep='\n')
