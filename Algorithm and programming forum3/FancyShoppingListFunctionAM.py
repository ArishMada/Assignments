from FancyShoppingListClasseAM import ShoppingList


# function to make the items and add them to a list
def make_objet_list():
    shopping_list = []
    num_of_items = eval(input('How many items are you going to buy? '))
    # number of item has to be greater than 1
    while num_of_items < 1:
        print("Number of items must be at least 1.")
        num_of_items = eval(input('How many items are you going to buy? '))
    else:
        for i in range(num_of_items):
            print(f'Item#{i + 1}')
            name = input('Enter the name of the item: ')
            amount = float(input('Enter the amount in pounds: '))
            while amount <= 0:
                print("Amount should be greater than 0")
                amount = eval(input('Enter the amount in pounds: '))

            # add the different items to the list
            shopping_list.append(ShoppingList(name.title(), amount))
    return shopping_list


# function to display the content of the list
def display_list(list_of_items):
    print("Here is the summary of the items purchased: "
          "\n----------------------------------")
    for item in list_of_items:
        print(item.__str__())


# function to get the total cost of all the items ordered
def calculate_amount(list_of_items):
    Total = 0
    for i in list_of_items:
        Total += i.Cost
    print(f'Total: ${Total}')


# call all the previous function into one
def main():
    shopping_list = make_objet_list()
    display_list(shopping_list)
    calculate_amount(shopping_list)


main()
