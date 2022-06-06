from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
 
    try:
        print(a.index(min(i for i in c if c[i] == 1)) + 1)
    except:
        print(-1)