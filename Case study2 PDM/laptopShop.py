inventory = {}
with open("inventory.txt") as f:
    for line in f:
        (key, val) = line.split()
        inventory[key] = int(val)
prices = {'Apple': 1200, 'Hp': 750, 'Dell': 980, 'Lenovo': 875, 'Acer': 1100, 'Asus': 700}

cost_per_item = []
shopping_list = []
quantity_of_item = []
num_of_items_desired = eval(input('Enter the number of items you wish to buy: '))
while num_of_items_desired < 1:
    print("Number of items must be at least 1.")
    num_of_items = eval(input('Re-enter the number of items you wish to buy: '))
else:
    for i in range(num_of_items_desired):
        brand = input("Enter the brand: ").title()
        while brand not in inventory.keys():
            print(f'We do not have {brand} in our inventory')
            more = input('Do you want to buy something else?(yes/no): ')
            if more == "yes":
                brand = input("Enter the brand: ").title()
            else:
                break
        else:
            shopping_list.append(brand)
            quantity = eval(
                input(f'Enter the quantity of laptop {brand} you would want to buy: '))
            while quantity < 1:
                print("quantity must be at least 1")
                quantity = eval(input(f'Enter the quantity of laptop {brand} you would want '
                                      f'to buy: '))
            else:
                while quantity > inventory[brand]:
                    print(f'We have only {inventory[brand]} in our inventory')
                    quantity = eval(
                        input(f'Enter the quantity of laptop {brand} you would want '
                              f'to buy: '))
                else:
                    inventory[brand] -= quantity
                    file = open("inventory.txt", "w")
                    for key, value in inventory.items():
                        file.write('%s %s\n' % (key, value))
                    file.close()

                    quantity_of_item.append(quantity)
                    cost = prices[brand] * quantity
                    cost_per_item.append(cost)

print('Here is the summary of your shopping:')
total = 0
for i in range(len(shopping_list)):
    total += cost_per_item[i]
    print(f'item: {shopping_list[i]} \nquantity: {quantity_of_item[i]} \ncost: '
          f'{cost_per_item[i]}$ \n------------')
print(f'Total cost of your shopping: {total}$')

