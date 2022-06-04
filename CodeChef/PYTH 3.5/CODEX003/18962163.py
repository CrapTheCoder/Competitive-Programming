r = ''
v = ['a', 'e', 'i', 'o', 'u']
n = input()

n = list(n)

for i in n:
    if i not in v:
        if i == ' ':
            r += i
        else:
            j = i + 'o' + i
            r += j
    else:
        r += i
print(r)
