def find_next(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if not grid[x][y]:
                return x, y

    for x in range(0, 9):
        for y in range(0, 9):
            if not grid[x][y]:
                return x, y

    return -1, -1

def valid(grid, i, j, e):
    rk = all([e != grid[i][x] for x in range(9)])

    if rk:
        ck = all([e != grid[x][j] for x in range(9)])

        if ck:
            stx, sty = 3 * (i // 3), 3 * (j // 3)

            for x in range(stx, stx + 3):
                for y in range(sty, sty + 3):
                    if grid[x][y] == e:
                        return False
            return True

    return False


def solve(grid, i=0, j=0):
    i, j = find_next(grid, i, j)

    if i == -1:
        return True

    for e in range(1, 10):
        if valid(grid, i, j, e):
            grid[i][j] = e

            if solve(grid, i, j):
                return True

            grid[i][j] = 0

    return False

grid = [list(map(int, input().split())) for r in range(9)]
solve(grid)

print(*(' '.join(str(j) for j in i) for i in grid), sep='\n')