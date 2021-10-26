# get the number of days from number of hours, minutes and seconds
def convert_to_days():
    h = float(input('Enter number of hours: '))
    m = eval(input('Enter number of minutes: '))
    s = eval(input('Enter number of seconds: '))

    def get_days():
        return round(h / 24 + m / 1440 + s / 86400, 4)

    print()
    print(f'The number of days is: {get_days()}')


convert_to_days()
