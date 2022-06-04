for _ in range(int(input())):
    s = input()

    if sorted('helloworld') == sorted(s):
        print('Yes')
    else:
        print('No')