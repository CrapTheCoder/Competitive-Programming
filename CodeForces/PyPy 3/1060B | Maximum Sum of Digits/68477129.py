n = int(input())
 
s = ''
 
while int(s + '9') <= n:
    s += '9'
 
if not s:
    s = '0'
 
print(sum(int(i) for i in s) + sum(int(i) for i in str(n - int(s))))