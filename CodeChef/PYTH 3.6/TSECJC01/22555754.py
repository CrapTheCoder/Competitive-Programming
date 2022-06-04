for _ in range(int(input())):
    l, d, h = map(int, input().split())

    print('No' if d / l > h else 'Yes')