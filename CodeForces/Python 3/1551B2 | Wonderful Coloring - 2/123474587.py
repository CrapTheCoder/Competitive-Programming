from collections import Counter
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    ind = {i: [] for i in a}
    for i, j in enumerate(a):
        ind[j].append(i)
 
    ans = [0] * n
    d = []
 
    for i in ind:
        if len(ind[i]) >= k:
            col = 1
            for j in ind[i][:k]:
                ans[j] = col
                col += 1
 
        else:
            d.append((len(ind[i]), i))
 
    d.sort()
 
    col = 0
    for i in d:
        for j in ind[i[1]]:
            ans[j] = col + 1
            col = (col + 1) % k
 
    c = Counter(ans)
    if 0 in c:
        c.pop(0)
 
    mini = min(c.values())
    for i in range(n):
        if c[ans[i]] > mini:
            c[ans[i]] -= 1
            ans[i] = 0
 
    print(*ans)