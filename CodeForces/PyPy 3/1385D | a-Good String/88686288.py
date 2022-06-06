def solve(s, c):
    n = len(s)
    
    if n == 1:
        return int(s != c)
    
    n //= 2
    
    return min(n - s[:n].count(c) + solve(s[n:], chr(ord(c) + 1)),
               n - s[n:].count(c) + solve(s[:n], chr(ord(c) + 1)))
 
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    print(solve(s, 'a'))