input()
s = input().split()

depth = mdepth = 0
depthi = 0

size = msize = 0
sizei = 0

lopen = 0

for i, j in enumerate(s):
    size += 1

    if j == '1': depth += 1
    if j == '2': depth -= 1

    if depth == 0:
        if msize < size:
            msize = size
            sizei = lopen

        lopen = i+1
        size = 0

    if mdepth < depth:
        mdepth = depth
        depthi = i

print(mdepth, depthi + 1, msize, sizei + 1)
