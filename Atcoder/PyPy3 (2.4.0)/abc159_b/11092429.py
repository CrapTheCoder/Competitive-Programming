s = input()
n = len(s)

x1 = s[:n//2]
x2 = s[n//2+1:]

if x1 == x1[::-1] and x2 == x2[::-1] and s == s[::-1]:
    print('Yes')
else:
    print('No')