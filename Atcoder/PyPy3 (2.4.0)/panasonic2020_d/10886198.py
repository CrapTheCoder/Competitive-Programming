from string import ascii_lowercase as alps

n = int(input())

def solve(x=n, c=0, l=[]):
    if x == 0:
        print(''.join(alps[i-1] for i in l))
        return

    x -= 1

    for nc in range(1, c + 1):
        solve(x, c, l + [nc])

    solve(x, c+1, l + [c+1])

solve()
