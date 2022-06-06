n, m = map(int,input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

mini = float('inf')

for i in range(n):
x = (b[0] - a[i]) % m

if sorted([(x + a[j]) % m for j in range(n)]) == b:
mini = min(mini, x)

print(mini)