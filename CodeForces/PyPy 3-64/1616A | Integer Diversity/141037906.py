from sys import stdin
input = stdin.readline
 
max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = set()
    for i in a:
        if i in s:
            s.add(-i)
        else:
            s.add(i)
 
    print(len(s))