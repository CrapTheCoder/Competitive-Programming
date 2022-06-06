n, x, y = map(int, input().split())
s = input()[::-1]
 
c = s[:x].count('1')
 
if s[y] == '0':
    c += 1
else:
    c -= 1
 
print(c)