
v = eval(input("Enter the plane's take off speed in m/s: "))
a = (eval(input("Enter the plane's acceleration in m/s**2: ")))

length_needed = (v**2) / (2*a)

print(f'The minimum runway length needed for this airplane is {round(lenght_needed,4)} meters')
