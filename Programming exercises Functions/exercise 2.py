# get your weight on another planet
def calc_weight(w_on_earth, g=23.1):
    m = w_on_earth / 9.8
    w_on_another_planet = m * g
    print(w_on_another_planet)

# sample input
calc_weight(120, 9.8)
calc_weight(120)
calc_weight(120, 23.1)

