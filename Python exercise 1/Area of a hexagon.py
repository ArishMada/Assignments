import math

side_length = eval(input('Enter the side length of the hexagon: '))
area = "{:,.3f}".format((3*math.sqrt(3)) / 2 * math.pow(side_length, 2))

print(f'The area of a hexagon with side length {side_length} is {area}')


