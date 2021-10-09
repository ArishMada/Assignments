import math
temperature_F = eval(input('Enter the temperature in Fahrenheit: '))

while True:
    if -58 < temperature_F < 41:
        wind_speed = eval(input('Enter the wind speed in miles per hour: '))
        while True:
            if wind_speed >= 2:
                twc = 35.74 + (0.6215 * temperature_F) - (35.75 * wind_speed ** 0.16) + (
                            0.4275 * temperature_F * wind_speed
                            ** 0.16)
                wind_chill_temperature = "{:,.3f}".format(twc)
                print(f'The wind chill index is {wind_chill_temperature}')
                break
            else:
                print('Speed must be greater than or equal to 2 mph')
                wind_speed = eval(input('Please re-enter the wind speed miles per hour: '))
        break
    else:
        print('Temperature must be between -58F and 41F')
        temperature_F = eval(input('Please re-enter the temperature in Fahrenheit: '))


