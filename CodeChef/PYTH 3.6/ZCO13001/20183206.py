n = int(input())
a = sorted(map(int, input().split()))

x = y = 0

for i in range(1, n):
    x += i * (a[i] - a[i - 1])
    y += x
    
print(y)