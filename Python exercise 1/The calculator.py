subtotal = eval(input('Enter the subtotal: $'))
tip = eval(input('Enter the tip amount (as a %): '))

Subtotal = "${:,.2f}".format(subtotal)
tip = subtotal * tip / 100
Tip = "${:,.2f}".format(tip)
total = tip + subtotal
Total = "${:,.2f}".format(total)

print(f'Subtotal: {Subtotal}')
print(f'Tip: {Tip}')
print(f'Total: {Total}')