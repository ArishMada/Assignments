class ShoppingList:
    # defining the initializer method with two parameters
    def __init__(self, name, amount):
        # name of the food-will be updated using the name parameter
        self.__name = name
        # amount in pounds-will be updated using the amount parameter
        self.__amount = amount
        # standard price/pound-will be updated using the a method
        self.__StandardPriceAM()
        # calculated price that will depend on the amount-will be updated
        # using the a method
        self.Cost = self.__calculatedCostAM()

    # getter methods
    def getStandardPriceAM(self):
        return self.__standard_price

    def getCostAM(self):
        return self.Cost

    # a method to define the standard price per pound of each item based on
    # their name
    def __StandardPriceAM(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__standard_price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__standard_price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__standard_price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__standard_price = 306.50
        elif self.__name == "Moose Cheese":
            self.__standard_price = 487.20
        elif self.__name == "White Truffles":
            self.__standard_price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__standard_price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__standard_price = 270.81
        else:
            self.__standard_price = 0.0
            print("Item not available or name misspelled")

    # calculate the cost of the order of each item
    def __calculatedCostAM(self):
        return float(self.__amount) * float(self.__standard_price)

    def __str__(self):
        return f'Item:{self.__name}\nAmount ordered: {self.__amount} pound(' \
               f's)\nPrice per pound: ${self.__standard_price}\nPrice of ' \
               f'order: ${self.Cost} '
