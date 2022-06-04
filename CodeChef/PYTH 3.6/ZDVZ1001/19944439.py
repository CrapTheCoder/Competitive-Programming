def reverse(n):
    rev = 0

    while n:
        rem = n % 10
        rev = 10 * rev + rem
        n = n // 10

    return rev

print(reverse(int(input())))