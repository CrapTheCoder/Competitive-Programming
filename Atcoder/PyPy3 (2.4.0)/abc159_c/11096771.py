def ans(s):
    length = s / 3

    s -= length

    breadth = s / 2
    height = s - breadth

    return length * breadth * height

l = int(input())

x = ans(l)

print('%.12f' % x)