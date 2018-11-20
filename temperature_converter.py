temp= eval(input('enter temperature in fahrenheit:'))
kelvin= (temp - 32) × 5/9 + 273.15
celsius= (temp - 32) × 5/9 
print('the result is {:.3f} kelvin and {:.3f} fahrenheit '.format(celsius, kelvin))
