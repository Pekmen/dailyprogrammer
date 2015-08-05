

m1, x1, y1 = map(float, raw_input('>').split(' '))
m2, x2, y2 = map(float, raw_input('>').split(' '))

print (m1 * m2) / (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2) ** 0.5
