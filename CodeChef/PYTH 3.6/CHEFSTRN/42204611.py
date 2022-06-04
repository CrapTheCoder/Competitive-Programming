s = input()

stk = []

for i in s:
    if stk and stk[-1] == i:
        stk.pop()
    else:
        stk.append(i)

if stk:
    print(*stk, sep='')
else:
    print('Empty String')