for _ in range(int(input())):
    s, w1, w2, w3 = map(int, input().split())

    print(-(-(w1+w2+w3) // s))