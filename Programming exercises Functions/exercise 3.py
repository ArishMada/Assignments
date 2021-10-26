# calculates how many atoms are in n grams of an element given its atomic weight
def num_atoms(amount, atomic_weight=196.97):
    moles = amount / atomic_weight
    number_of_atoms = moles * (6.022*10**23)

    print(number_of_atoms)

# sample input
num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)

