l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = 0

    for i in str(a+b):
        c += l[int(i)]

    print(c)