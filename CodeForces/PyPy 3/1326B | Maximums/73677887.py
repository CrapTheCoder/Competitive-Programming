n = int(input())
b = list(map(int, input().split()))
 
m = 0
a = [b[0]]
 
for i in range(1, n):
    m = max(a[-1], m)
 
    a.append(b[i] + m)
 
print(*a)