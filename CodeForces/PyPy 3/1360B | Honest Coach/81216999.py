for _ in range(int(input())):
n = int(input())
a = sorted(map(int, input().split()))

mini = float('inf')

for i in range(1, n):
if a[i] - a[i-1] < mini:
mini = a[i] - a[i-1]

print(mini)