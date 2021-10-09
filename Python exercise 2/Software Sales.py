nopp = int(input('Enter the number of packages purchased: '))
amount = 99 * nopp

if nopp < 10:
    discount = 0 * amount / 100
    Discount = "$ {:.2f}".format(discount)
    print(f'Discount amount @ 0%: {Discount}')
    total_amount = "$ {:.2f}".format(amount - discount)
    print(f'Total amount: {total_amount}')
elif 10 <= nopp <= 19:
    discount = 10 * amount / 100
    Discount = "$ {:.2f}".format(discount)
    print(f'Discount amount @ 10%: {Discount}')
    total_amount = "$ {:.2f}".format(amount - discount)
    print(f'Total amount: {total_amount}')
elif 20 <= nopp <= 49:
    discount = 20 * amount / 100
    Discount = "$ {:.2f}".format(discount)
    print(f'Discount amount @ 20%: {Discount}')
    total_amount = "$ {:.2f}".format(amount - discount)
    print(f'Total amount: {total_amount}')
elif 50 <= nopp <= 99:
    discount = 30 * amount / 100
    Discount = "$ {:.2f}".format(discount)
    print(f'Discount amount @ 30%: {Discount}')
    total_amount = "$ {:.2f}".format(amount - discount)
    print(f'Total amount: {total_amount}')
else:
    discount = 40 * amount / 100
    Discount = "$ {:.2f}".format(discount)
    print(f'Discount amount @ 40%: {Discount}')
    total_amount = "$ {:.2f}".format(amount - discount)
    print(f'Total amount: {total_amount}')




