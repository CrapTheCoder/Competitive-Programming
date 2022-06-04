vows = 'AEIOU'

s = input()
n = len(s)

f1 = f2 = False

for i in range(2, n):
    if (s[i] in vows) and (s[i-1] in vows) and (s[i-2] in vows):
        f1 = True

if len(set(i for i in s if i not in vows)) >= 5:
    f2 = True

print([-1, 'GOOD'][f1 == f2 == True])
