from fractions import Fraction

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a, b = sorted([a, b])

    f = Fraction(b-c, c-a)

    print(f.numerator, f.denominator)
