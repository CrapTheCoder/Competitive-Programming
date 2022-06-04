for _ in range(int(input())):
    t, a, b = input().split()

    if sorted(t) == sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Not Possible')
