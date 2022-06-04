def swap(i1, i2, i3):
    answer.append((i1, i2, i3))

    a[i1], a[i2], a[i3] = a[i3], a[i1], a[i2]
    i1, i2, i3 = i3, i1, i2

    d[i1] = i1
    d[i2] = i2
    d[i3] = i3

def size3():
    for i in range(n):
        if a[i] == i:
            continue

        while a[i] != i:
            i1, i2, i3 = i, a[i], a[a[i]]

            if len({i1, i2, i3}) != 3:
                break

            swap(i1, i2, i3)

def size2():
    global impossible

    for i in range(n):
        if a[i] == i:
            continue

        i1, i2, i3 = i, a[i], a[a[i]]

        for i3 in range(i+1, n):
            if i3 != i1 and i3 != i2 and a[i3] != i3:
                break
        else:
            impossible = True
            break

        swap(i1, i2, i3)

        if a[i1] == i1:
            continue

        i1, i2, i3 = i1, a[i1], a[a[i1]]

        swap(i1, i2, i3)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] -= 1

    d = {a[i]: i for i in range(n)}

    answer = []
    impossible = False

    size3()
    size2()

    if impossible or a != sorted(a):
        print(-1)
        continue

    print(len(answer))

    for (i1, i2, i3) in answer:
        print(i1+1, i2+1, i3+1)
