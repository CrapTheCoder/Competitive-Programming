for _ in range(int(input())):
    s = input().strip()
    input()
    a = set(input().split())

    d = set(s)

    print(int(all(i in a for i in d)))
