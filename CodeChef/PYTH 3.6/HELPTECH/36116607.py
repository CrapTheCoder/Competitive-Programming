for _ in range(int(input())):
    n = int(input())
    s = 0

    l = []

    for i in range(n):
        name, number, marks = input().split()
        marks = int(marks)
        s += marks

        l.append([name, number, marks])

    s /= n

    l.sort(key=lambda x: x[-1])

    for i in l:
        if i[-1] < s:
            print(i[0] + ' ' + i[1] + ' ' + str(i[-1]))
