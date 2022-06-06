def f1(i, j):
    for i in range(i, j):
        if s[i:j+1] == s[i:j+1][::-1]:
            return s[i:j+1]
 
    return ''
 
def f2(i, j):
    for j in range(j, i-1, -1):
        if s[i:j+1] == s[i:j+1][::-1]:
            return s[i:j+1]
 
    return ''
 
for _ in range(int(input())):
    s = input()
 
    if s == s[::-1]:
        print(s)
        continue
 
    n = len(s)
 
    tp = ''
    ts = ''
 
    i = 0
 
    for i in range(n // 2):
        if s[i] == s[n-i-1]:
            tp += s[i]
            ts += s[i]
        else:
            break
 
    x1 = f1(i, n-i-1)
    x2 = f2(i, n-i-1)
 
    y1 = tp + ts[::-1]
    y2 = tp + ts[::-1]
 
    z1 = tp + x1 + ts[::-1]
    z2 = tp + x2 + ts[::-1]
 
    if len(z1) <= n: y1 = z1
    if len(z2) <= n: y2 = z2
 
    print(max(y1, y2, key=len))