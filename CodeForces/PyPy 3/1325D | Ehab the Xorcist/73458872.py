u, v = map(int, input().split())

if u > v or (v - u) & 1:
print(-1)
exit()

if u == v:
if u == 0:
print(0)
else:
print(1)
print(u)

exit()

e = (v - u) >> 1

if (u + e) ^ e == u:
print(2)
print(u + e, e)
else:
print(3)
print(u, e, e)