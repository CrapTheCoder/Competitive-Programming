n = int(input())
a = list(map(int, input().split()))

mnl = cnl = 0
mni = -1

mml = cml  = 0
mmi = cmi = 0

for i in range(n):
    cml += 1

    if a[i] == 1:
        cnl += 1

    else:
        if cnl > mnl:
            mnl = cnl
            mni = i

        cnl -= 1

    if not cnl:
        if cml > mml:
            mml = cml
            mmi = cmi

        cml = 0
        cmi = i + 1

print(mnl, mni, mml, mmi + 1)