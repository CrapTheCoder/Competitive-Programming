from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
 
    for x in range(1, 1025):
        if sorted(i ^ x for i in a) == a:
            print(x)
            break
    else:
        print(-1)