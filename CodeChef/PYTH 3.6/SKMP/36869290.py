from collections import Counter

for _ in range(int(input())):
    s = input()
    p = input()

    d = ''.join(sorted((Counter(s) - Counter(p)).elements()))

    first = ''
    flag = False

    mini = d + p

    for i in range(len(d)):
        if d[i] >= p[0]:
            if not first:
                mini = min(mini, d[:i] + p + d[i:])
                first = d[i]

            elif d[i] != first and not flag:
                mini = min(mini, d[:i] + p + d[i:])
                flag = True

    print(mini)
