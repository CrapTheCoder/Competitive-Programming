for _ in range(int(input())):
    d = int(input())

    dps = []

    for i in range(d):
        dps.append(list(map(int, input().split())))

    dps = sorted(dps)
    q = int(input())

    for l in range(q):
        dead, req = map(int, input().split())
        probs = 0

        for i in dps:
            if i[0] > dead: break
            else: probs += i[1]

        print('Go ' + ['Sleep', 'Camp'][probs >= req])