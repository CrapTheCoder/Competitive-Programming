n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

maxi = max(a) + m

while m:
a[a.index(min(a))] += 1
m -= 1

mini = max(a)

print(mini, maxi)