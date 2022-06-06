from string import ascii_lowercase as alps
 
for _ in range(int(input())):
    n, a, b = map(int, input().split())
 
    s = ''
 
    for i in range(n):
        s += alps[i % b]
 
    print(s)