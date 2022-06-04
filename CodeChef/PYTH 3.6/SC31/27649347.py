for _ in range(int(input())):
    n = int(input())

    l = [0] * 10

    for __ in range(n):
        s = input()

        for j in range(10):
            if s[j] == '1':
                l[j] += 1

    print(sum(i % 2 for i in l))
