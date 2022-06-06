n = int(input())
a = sorted(map(int, input().split()))
 
s = 0
 
for i in range(n // 2):
    s += (a[i] + a[-i-1]) ** 2
 
print(s)