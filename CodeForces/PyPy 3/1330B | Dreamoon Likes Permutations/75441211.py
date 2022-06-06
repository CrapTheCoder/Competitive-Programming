for _ in range(int(input())):
n = int(input())
a = list(map(int, input().split()))

min1 = float('inf')
max1 = 0

s1 = set()
is_perm_pref = [False]

for i in range(n):
min1 = min(min1, a[i])
max1 = max(max1, a[i])

s1.add(a[i])

if len(s1) == i+1 and min1 == 1 and max1 == i + 1:
is_perm_pref.append(True)
else:
is_perm_pref.append(False)

min2 = float('inf')
max2 = 0

s2 = set()
is_perm_suff = [False]

for i in range(n-1, -1, -1):
min2 = min(min2, a[i])
max2 = max(max2, a[i])

s2.add(a[i])

if len(s2) == n - i and min2 == 1 and max2 == n - i:
is_perm_suff.append(True)
else:
is_perm_suff.append(False)

is_perm_suff.reverse()

ans = []

for i in range(n+1):
if is_perm_pref[i] and is_perm_suff[i]:
ans.append((i, n-i))

print(len(ans))

for i in ans:
print(*i)