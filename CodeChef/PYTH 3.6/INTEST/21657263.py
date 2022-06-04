n, k = map(int, input().split())
c = 0

for _ in range(n):
    i = int(input())
    
    c += not i % k

print(c)