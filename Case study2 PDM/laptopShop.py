brands = ["Apple", "Hp", "Dell", "Lenovo", "Acer", "Asus"]
inventory = {'Apple': 2}
prices = {'Apple': 12}

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
        if brand in brands:
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
                    quantity_of_item.append(quantity)
                    cost = prices[brand] * quantity
                    cost_per_item.append(cost)

        else:
            print(f'We do not have {brand} in our inventory')
            more = input('Do you want to buy something else?(yes/no): ')
            if more == "yes":
                brand = input("Enter the brand: ").title()
            else:
                break
print('Here is the summary of your shopping:')
total = 0
for i in range(len(shopping_list)):
    total += cost_per_item[i]
    print(f'item: {shopping_list[i]} \nquantity: {quantity_of_item[i]} \ncost: '
          f'{cost_per_item[i]} \n------------')
print(f'Total cost of your shopping: {total}$')

print(inventory)