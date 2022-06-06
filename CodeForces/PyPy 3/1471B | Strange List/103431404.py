from sys import stdin
from collections import deque, Counter
 
input = stdin.readline
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
 
    cnt = Counter(a)
 
    b = deque()
    c = deque()
 
    st = set()
    for i in a:
        b.append(i)
        c.append(1)
 
    s = 0
    while True:
        if b[0] % x != 0:
            break
 
        b.append(b[0] // x)
        c.append(c[0] * x)
 
        s += b.popleft() * c.popleft()
 
    print(s + sum(i * j for i, j in zip(b, c)))