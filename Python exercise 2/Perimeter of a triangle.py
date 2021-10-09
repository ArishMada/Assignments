e1 = eval(input("Enter length of edge1: "))
e2 = eval(input("Enter length of edge2: "))
e3 = eval(input("Enter length of edge3: "))

if e1 + e2 > e3 and e2 + e3 > e1 and e3 + e1 > e2:
    perimeter = e3 + e2 + e1
    print(f'The perimeter is {round(perimeter, 1)}')
else:
    print("Perimeter cannot be calculated: the input is invalid")