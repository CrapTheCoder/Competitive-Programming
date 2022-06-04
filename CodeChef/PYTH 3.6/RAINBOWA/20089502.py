for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))

    x = 0

    new = c[:1]

    for i, j in enumerate(c[1:], 1):
        if j == c[i - 1]:
            continue
        else:
            new.append(j)

    print('yes' if new == [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1] and c[::-1] == c else 'no')