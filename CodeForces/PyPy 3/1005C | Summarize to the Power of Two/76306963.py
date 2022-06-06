from collections import Counter

pows = [1]

for i in range(64 + 1):
pows.append(pows[-1] * 2)

n = int(input())
a = list(map(int, input().split()))

x = Counter(a)

ans = 0

for i in a:
for p in pows:
j = p - i

if j in x:
if i == j:
if x[i] >= 2:
break
else:
break
else:
ans += 1

print(ans)