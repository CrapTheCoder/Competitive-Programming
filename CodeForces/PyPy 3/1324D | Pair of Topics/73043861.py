n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a[i] - b[i] for i in range(n))

i = 0
j = n - 1

ans = 0

while i < j:
while c[i] + c[j] <= 0 and i < j:
i += 1

ans += j - i

j -= 1

print(ans)