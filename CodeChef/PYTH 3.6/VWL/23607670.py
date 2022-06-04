d = {'a', 'e', 'i', 'o', 'u'}

n = int(input())
s = input()

for i in s:
    if i in d: d.remove(i)

if len(d) <= 1:
    print('Yes')
else:
    print('No')