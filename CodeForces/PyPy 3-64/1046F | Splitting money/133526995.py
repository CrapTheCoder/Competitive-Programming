n = int(input())
a = list(map(int, input().split()))
x, f = map(int, input().split())
 
s = 0
for i in a:
    s += -(-(i-x) // (x + f)) * f
 
print(s)