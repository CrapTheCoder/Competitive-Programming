for _ in range(int(input())):
    s1 = input()
    s2 = input()

    dum = list(zip(*sorted(zip(s1, s2))))
    l1, l2 = list(dum[0]), list(dum[1])
    d1, d2, d3 = l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2]

    b1 = list('bbo')
    b2 = list('bob')
    b3 = list('obb')

    if (b1[0] in d1 and b1[1] in d2 and b1[2] in d3) or\
       (b2[0] in d1 and b2[1] in d2 and b2[2] in d3) or\
       (b3[0] in d1 and b3[1] in d2 and b3[2] in d3):
        print('yes')
    else:
        print('no')