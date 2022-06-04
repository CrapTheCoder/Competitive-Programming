def s1(s):
    try:
        c = 0
        i = s.index('5')
        c += i
        s = s[i+1:]
        j = min(s.index('2') if '2' in s else float('inf'), s.index('7') if '7' in s else float('inf'))
        c += j
        return c
 
    except:
        return float('inf')
 
 
def s2(s):
    try:
        c = 0
        i = s.index('0')
        c += i
        s = s[i+1:]
        j = min(s.index('5') if '5' in s else float('inf'), s.index('0') if '0' in s else float('inf'))
        c += j
        return c
 
    except:
        return float('inf')
 
 
for _ in range(int(input())):
    s = input()[::-1]
 
    print(min(s1(s), s2(s)))