s = input()
 
c = {}
d = {}
 
for i in s:
    c[i] = c.get(i, 0) + 1
 
    for j, k in c.items():
        if i != j:
            d[i + j] = d.get(i + j, 0) + k
 
x = max(c.values())
y = max(d.values()) if d else 0
z = max(i * (i - 1) // 2 for i in c.values())
 
print(max(x, y, z))