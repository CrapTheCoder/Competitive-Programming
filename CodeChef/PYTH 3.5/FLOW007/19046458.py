for i in range(int(input())):
    n = int(input())
    rev = 0

    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10

    print(rev)