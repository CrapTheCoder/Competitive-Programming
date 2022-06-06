s = input()
n = len(s)
 
x1, x2 = [], []
ops = [i for i in range(n) if s[i] == '('][::-1]
cls = [i for i in range(n) if s[i] == ')']
 
while ops and cls and ops[-1] < cls[-1]:
    x1.append(str(ops.pop() + 1))
    x2.append(str(cls.pop() + 1))
 
if len(x1 + x2) == 0:
    print(0)
 
else:
    print(1)
    print(len(x1 + x2))
    print(*x1 + x2[::-1])