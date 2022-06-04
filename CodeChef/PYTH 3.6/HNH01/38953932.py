for _ in range(int(input())):
    print(sum(c.isupper() and c.isalpha() for c in input().strip()))
