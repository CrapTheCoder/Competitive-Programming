from collections import Counter
from itertools import permutations
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    m = n // 3
 
    c = Counter(i % 3 for i in a)
    t = 0
 
    for (i, j) in permutations([0, 1, 2], 2):
        if c[i] > m:
            if c[j] < m:
                x = min(c[i] - m, m - c[j])
                c[j] += x
                c[i] -= x
                t += x * ((j - i) % 3)
 
    print(t)