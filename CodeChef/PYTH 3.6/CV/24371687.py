v = 'aeiou'

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    c = 0
    
    for i in range(n-1):
        if s[i] not in v and s[i+1] in v:
            c += 1
    
    print(c)