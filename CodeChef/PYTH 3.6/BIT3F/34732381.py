v = 'aeiou'

for _ in range(int(input())):
    s = input().strip()
    
    c = 0
    
    for i in s:
        c += min(abs(ord(i) - ord(j)) for j in v)
    
    print(c)