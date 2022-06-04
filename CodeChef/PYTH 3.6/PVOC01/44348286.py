for _ in range(int(input())):
    n = int(input())
    s = bin(n)[2:][::-1]

    l = []

    j = 1
    for i in s:
        if i == '1':
            l.append(j)

        j *= 3

    print(len(l))
    print(* l)
