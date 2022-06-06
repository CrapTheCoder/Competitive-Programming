for _ in range(int(input())):
n = int(input())

mini = float('inf')

for i in range(max(1, int(n ** 0.5) - 5), int(n ** 0.5) + 6):
mini = min(mini, -(-n // i) + i)

print(mini - 2)