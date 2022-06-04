n = int(input())

l1 = [0]
l2 = [0]

s1 = s2 = 0

for _ in range(n):
    p1, p2 = map(int, input().split())

    s1 += p1
    s2 += p2

    if s1 > s2: l1.append(s1 - s2)
    if s1 < s2: l2.append(s2 - s1)

if max(l1) > max(l2): print(1, max(l1))
if max(l1) < max(l2): print(2, max(l2))
