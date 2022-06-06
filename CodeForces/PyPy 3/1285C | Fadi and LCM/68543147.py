from math import sqrt
from collections import Counter
 
def poss(i=0, c=1):
    if i == m:
        subs.append(c)
        return
 
    poss(i+1, c)
    poss(i+1, c * a[i])
 
def facts(x):
    while x % 2 == 0:
        l.append(2)
        x //= 2
 
    for i in range(3, int(sqrt(x)) + 1, 2):
        while x % i == 0:
            l.append(i)
            x //= i
 
    if x > 1:
        l.append(x)
 
l = []
subs = []
 
x = int(input())
facts(x)
 
c = Counter(l)
 
a = sorted(i ** c[i] for i in c.keys())
 
l = r = 1
 
for i in a:
    r *= i
 
i = 0
 
cm = r
 
m = len(a)
 
poss()
 
l = min(subs, key=lambda y: max(y, x // y))
r = x // l
 
if l > r:
    l, r = r, l
 
print(l, r)