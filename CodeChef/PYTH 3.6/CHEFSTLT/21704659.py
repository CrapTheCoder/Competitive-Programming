for _ in range(int(input())):
    a = input()
    b = input()

    min = 0
    max = 0

    for i, j in zip(a, b):
        if '?' in [i, j]:
            max += 1
        else:
            if i != j:
                min += 1
                max += 1

    print(min, max)