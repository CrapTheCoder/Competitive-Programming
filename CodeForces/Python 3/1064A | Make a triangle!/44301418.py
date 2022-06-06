a, b, c = map(int, input().split())
 
m = max(a, b, c)
 
x = y = -1
 
if m == a:
    x = b
    y = c
 
if m == b:
    x = a
    y = c
 
if m == c:
    x = a
    y = b
 
print(max((m - (x + y)) + 1, 0))