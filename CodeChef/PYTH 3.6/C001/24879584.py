q = int(input())
s = ''
l = []

for i in range(q):
    x = list(input().split())
    a = int(x[0])

    if a == 1:
        l.append(s)
        s += x[1]

    elif a == 2:
        l.append(s)
        s = s[0:len(s)-int(x[1])]

    elif a == 3:
        print(s[int(x[1]) - 1])

    else:
        s = l[len(l) - 1]
        l.pop(len(l) - 1)