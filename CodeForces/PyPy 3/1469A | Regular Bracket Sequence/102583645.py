def solve(s):
    c = t = 0
    for i in s:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        else:
            t += 1
 
        if c+t < 0:
            return False
 
    return True
 
for _ in range(int(input())):
    s = input()
    s2 = s[::-1].replace('(', '~').replace(')', '(').replace('~', ')')
 
    if len(s) % 2:
        print('NO')
        continue
 
    if solve(s) and solve(s2):
        print('YES')
    else:
        print('NO')