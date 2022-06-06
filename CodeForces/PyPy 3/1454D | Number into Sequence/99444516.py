from functools import reduce
 
for _ in range(int(input())):
    n = int(input())
    nn = n
 
    ps = {}
 
    for i in range(2, int(n ** 0.5) + 1):
        if nn % i == 0:
            ps[i] = 0
            while nn % i == 0:
                nn //= i
                ps[i] += 1
 
    if nn > 1:
        ps[nn] = ps.get(nn, 0) + 1
 
    l = max(ps.keys(), key=ps.get)
    a = [l] * (ps[l] - 1)
 
    a.append(n // reduce(int.__mul__, a, 1))
 
    print(len(a))
    print(*a)