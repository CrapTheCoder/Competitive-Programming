a, b, c = int(input()), int(input()), int(input())

print('%.8f' % (((-b) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))
print('%.8f' % (((-b) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)))