from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    s = input().strip()
    print(*sorted(s), sep='')