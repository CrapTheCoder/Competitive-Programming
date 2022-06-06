for _ in range(int(input())):
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

for i in range(k):
if a[i] < b[n-i-1]:
a[i], b[n-i-1] = b[n-i-1], a[i]
else:
break

print(sum(a))