import sys
tokens = ''.join(sys.stdin.readlines()).split()[::-1]

def next(): return tokens.pop()
def nextInt(): return int(next())
def nextFloat(): return float(next())
def getIntArray(n): return [nextInt() for _ in range(n)]
def getFloatArray(n): return [nextFloat() for _ in range(n)]
def getStringArray(n): return [next() for _ in range(n)]


testcase = True
def solve(testcase=1):
    ver = "AHIMOTUVWXY"
    hor = "BCDEHIKOX"

    n = nextInt()
    s = getStringArray(n)

    l = []
    for i in s:
        f = ''
        for j in i:
            if j in ver and j in hor:
                f += '10'
            elif j in ver:
                f += '0'
            elif j in hor:
                f += '1'
            else:
                f += '01'

        l.append(int(f, 2))

    print(*l)


if testcase is None:
    testcaseCount = 1
    while tokens:
        solve(testcaseCount)
        testcaseCount += 1
else:
    testcaseCount = nextInt() if testcase else 1
    for tc in range(testcaseCount):
        solve(tc + 1)
    assert not tokens
