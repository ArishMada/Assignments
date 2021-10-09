import math

m = eval(input('Enter the mass of the cart (in kg): '))
f = eval(input('Enter the force to push the cart (in N): '))
g = 9.8

a = math.degrees(math.asin(f / m /g))
A = round(a, 1)
print(f'The angle of the ramp is {A} degrees')
