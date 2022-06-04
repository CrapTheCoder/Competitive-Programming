k = int(input())
o = k
a, b = list(map(int, input().split()))

while k <= b:
    if a <= k <= b:
        print('OK')
        break

    k += o

else:
    print('NG')