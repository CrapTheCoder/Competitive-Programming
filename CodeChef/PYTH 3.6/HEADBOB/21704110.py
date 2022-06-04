for _ in range(int(input())):
    n = int(input())
    s = input()

    if ('Y' not in s) and ('I' not in s):
        print('NOT SURE')
    elif 'Y' in s:
        print('NOT INDIAN')
    else:
        print('INDIAN')