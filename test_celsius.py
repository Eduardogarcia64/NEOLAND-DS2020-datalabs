fahrenheit = input()
if fahrenheit.isalpha():
    print('what is the temperature in fahrenheit?:'+ fahrenheit)
    print('input is not a number')
else:
    print('What is the temperature in fahrenheit?: ' + str(fahrenheit))
    print('temperature in celsius is: '+ str(int(fahrenheit)-32 * 5/9))