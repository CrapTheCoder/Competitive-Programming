for _ in range(int(input())):
n, x, y, d = map(int, input().split())

if abs(x - y) % d == 0:
print(abs(x - y) // d)
else:
mini = float('inf')

if (y-1) % d == 0:
mini = min(mini, (y-1) // d + -(-(x-1) // d))

if (n-y) % d == 0:
mini = min(mini, (n-y) // d + -(-(n-x) // d))

if mini == float('inf'):
print(-1)
else:
print(mini)