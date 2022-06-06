s = input()
n = len(s)
 
ops = []
cls = []
 
for i in range(n):
    if s[i] == '(':
        ops.append(i)
    else:
        cls.append(i)
 
ops.reverse()
 
k = 0
 
ans = ''
 
while True:
    c = 0
 
    x1 = []
    x2 = []
 
    while ops and cls and ops[-1] < cls[-1]:
        x1.append(str(ops.pop() + 1))
        x2.append(str(cls.pop() + 1))
 
        c += 1
 
    if c == 0:
        break
 
    x2.reverse()
 
    ans += str(c * 2) + '\n' + ' '.join(x1 + x2)
 
    k += 1
 
print(k)
print(ans)