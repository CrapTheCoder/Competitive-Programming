from sys import stdin
input = stdin.readline
 
max = lambda x, y: x if x > y else y
# min = lambda x, y: x if x < y else y
 
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
 
    t = s[0]
    for i in range(1, n):
        if s[i] < s[i-1]:
            t += s[i]
        elif len(t) != 1 and s[i] == s[i-1]:
            t += s[i]
        else:
            break
 
    print(t + t[::-1])