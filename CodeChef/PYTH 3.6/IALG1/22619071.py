from decimal import Decimal, getcontext
getcontext().prec = 110

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(Decimal(round(Decimal(a) / Decimal(b), 100)).normalize())
