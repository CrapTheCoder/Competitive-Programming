from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c = Counter(a)

    for i in a:
        if 2000 - i == i:
            if c[2000 - i] >= 2:
                print('Accepted')
                break

        else:
            if c[2000 - i] >= 1:
                print('Accepted')
                break
    else:
        print('Rejected')
