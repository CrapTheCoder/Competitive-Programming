n = int(input())
s = input()
 
if s.count('(') != s.count(')'):
    print(-1)
    exit()
 
v = [0]
 
for i in s:
    if i == '(': v.append(v[-1] + 1)
    if i == ')': v.append(v[-1] - 1)
 
c = 0
 
i = 0
 
while i < len(v):
    if v[i] < 0:
        while True:
            c += 1
 
            if v[i] == 0:
                break
 
            i += 1
 
    i += 1
 
print(c)