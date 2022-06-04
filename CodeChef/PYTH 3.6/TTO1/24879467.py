n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print('OK')

elif n == 2:
    if a[0] > a[1]:
        print(1)
    else:
        print('OK')

else:
    while True:
        b = a.copy()

        for i in range(n-2):
            pass

        if a == b:
            break

    for i in range(n-1):
        pass
    else:
        print('OK')
