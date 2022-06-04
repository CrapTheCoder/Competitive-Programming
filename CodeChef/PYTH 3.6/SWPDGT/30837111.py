def get_int(l):
    return int(''.join(l))

for _ in range(int(input())):
    s1, s2 = map(list, input().split())

    maxi = get_int(s1) + get_int(s2)

    for i in range(len(s1)):
        for j in range(len(s2)):
            s1[i], s2[j] = s2[j], s1[i]

            maxi = max(maxi, get_int(s1) + get_int(s2))

            s1[i], s2[j] = s2[j], s1[i]

    print(maxi)