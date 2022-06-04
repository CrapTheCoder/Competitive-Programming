from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 9)

"""

GREEN  = 0
RED    = 1
BLUE   = 2
YELLOW = 3
PINK   = 4

    0 1 2 3 4
  +-----------+
0 | X 0 1 X X |
1 | X 0 1 X X |
2 | X X 1 0 X |
3 | X X 1 X 0 |
4 | 0 X 1 X X |
  +-----------+

"""

g = [
    'X01XX',
    'X01XX',
    'XX10X',
    'XX1X0',
    '0X1XX'
]

n = 5

def dfs(u = 1):
    global s

    if not s:
        return u == 0

    for v in range(n):
        if g[u][v] == s[-1]:
            s.pop()

            if dfs(v):
                return True

            s += g[u][v]

    return False

def f1():
    if not s: return False

    x = s.pop()

    if x == '0': return f1()
    if x == '1': return f2()

def f2():
    if not s: return False

    x = s.pop()

    if x == '0': return f3()
    if x == '1': return f2()

def f3():
    if not s: return False

    x = s.pop()

    if x == '0': return f4()
    if x == '1': return f2()

def f4():
    if not s: return False

    x = s.pop()

    if x == '0': return f0()
    if x == '1': return f2()

def f0():
    if not s: return True

    x = s.pop()

    if x == '0': return f1()
    if x == '1': return f2()

for _ in range(int(input())):
    s = list(input().strip())[::-1]

    if f1():
        print('YES')
    else:
        print('NO')
