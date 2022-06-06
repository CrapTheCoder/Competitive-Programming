n, m = map(int, input().split())
 
d = {}
 
f = []
a = []
 
used = [False] * n
 
for i in range(n):
    s = input()
 
    if s[::-1] in d:
        used[i] = True
        used[d[s[::-1]]] = True
        f = [s] + f + [s[::-1]]
        del d[s[::-1]]
    else:
        d[s] = i
 
    a.append(s)
 
if len(f) % 2:
    print(len(f) * m)
    print(''.join(f))
else:
    for i in range(n):
        if not used[i] and a[i] == a[i][::-1]:
            f = f[:len(f) // 2] + [a[i]] + f[len(f) // 2:]
            break
 
    print(len(f) * m)
    print(''.join(f))