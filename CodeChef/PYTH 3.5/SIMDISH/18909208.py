def setint(set1, set2):
    ans = set(set1).intersection(set2)
    list(ans)
    if (ans.__len__()) >= 2:
        a = 'similar'

    else:
        a = 'dissimilar'

    return a

for i in range(int(input())):

    ing1 = input().split()
    ing2 = input().split()
    list(ing1)
    list(ing2)

    print(setint(ing1, ing2))
