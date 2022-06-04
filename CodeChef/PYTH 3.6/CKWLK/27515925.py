from math import log

for _ in range(int(input())):
    n = input()

    if round(log(int(n), 10), 2).is_integer():
        print('Yes')
    else:
        y = round(log(int(n.strip('0')), 2), 1)

        if y.is_integer():
            n = int(n)

            x = round(log(n / (2 ** y * 10 ** y), 10), 2)

            print('Yes' if x.is_integer() and x >= 0 else 'No')
        else:
            print('No')
