def factors(n):
for i in range(1, int(n ** 0.5) + 1):
if n % i == 0:
yield i

if n // i != i:
yield n // i

for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

cs = [1] * n

for i in range(n):
for j in factors(i+1):
j -= 1

if a[i] > a[j]:
cs[i] = max(cs[i], cs[j]+1)

print(max(cs))