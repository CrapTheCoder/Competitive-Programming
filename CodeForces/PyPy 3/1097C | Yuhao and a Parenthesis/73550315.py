def count(s):
    m = 0
    c = 0
 
    for i in s:
        if i == '(': c += 1
        if i == ')': c -= 1
 
        m = min(m, c)
 
    return c, m
 
n = int(input())
d = {}
 
for _ in range(n):
    c, m = count(input())
 
    if not (m < 0 and m < c):
        d[c] = d.get(c, 0) + 1
 
ans = 0
 
for i in d.keys():
    if -i in d:
        if i == 0:
            ans += d[i] // 2
        else:
            ans += min(d[i], d[-i])
            d[i] = d[-i] = 0
 
print(ans)