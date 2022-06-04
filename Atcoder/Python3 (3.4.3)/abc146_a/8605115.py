n = int(input())
a = list(map(int, input().split()))

prefix = [0]

for i in a:
    prefix.append(prefix[-1] + i)

mini = float('inf')

for i in range(0, n):
    mini = min(abs(prefix[i] - (prefix[-1] - prefix[i])), mini)

print(mini)
