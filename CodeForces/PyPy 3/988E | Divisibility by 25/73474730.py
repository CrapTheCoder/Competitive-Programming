def solve1():
    n = m
 
    try:
        x = n.index('0')
        n = n[x] + n[:x] + n[x+1:]
 
        x += len(n) - len(n.rstrip('0'))
 
        y = n.index('5')
 
        return x + y - 1
 
    except:
        return float('inf')
 
 
def solve2():
    n = m
 
    try:
        x = n.index('0')
        y = n.find('0', x+1)
 
        if y == -1:
            raise Exception
 
        return x + y - 1
 
    except:
        return float('inf')
 
 
def solve3():
    n = m
 
    try:
        x = n.index('5')
        n = n[x] + n[:x] + n[x+1:]
 
        x += len(n) - len(n.rstrip('0'))
 
        y = n.index('2')
 
        return x + y - 1
 
    except:
        return float('inf')
 
 
def solve4():
    n = m
 
    try:
        x = n.index('5')
        n = n[x] + n[:x] + n[x+1:]
 
        x += len(n) - len(n.rstrip('0'))
 
        y = n.index('7')
 
        return x + y - 1
 
    except:
        return float('inf')
 
m = input()[::-1]
 
x = min(
    solve1(),
    solve2(),
    solve3(),
    solve4()
)
 
if x == float('inf'):
    print(-1)
else:
    print(x)