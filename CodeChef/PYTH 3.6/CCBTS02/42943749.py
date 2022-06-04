for _ in range(int(input())):
    n = int(input())
    a = input().split()

    f = 0

    for i in a:
        if i == 'start' or i == 'restart':
            f = 1

        else:
            if not f:
                print(404)
                break

            f = 0

    else:
        print(200)
