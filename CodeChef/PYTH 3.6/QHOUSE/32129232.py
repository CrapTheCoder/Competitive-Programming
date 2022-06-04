MAX = 1000

def search(t, start=0):
    l, r = 0, MAX

    while l < r:
        m = -(-(l + r) // 2)

        if t == 'x':
            print('?', m, start)
        if t == 'y':
            print('?', start, m)

        if input() == 'YES':
            l = m
        else:
            r = m-1

    return l

square_side = search('x') * 2

triangle_base = search('x', square_side) * 2
triangle_height = search('y') - square_side

area = square_side * square_side + (triangle_base * triangle_height) // 2

print('!', area)
