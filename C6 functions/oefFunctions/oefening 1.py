def celcius_fahrenheit(degree):
    fahrenheit = (degree*(9/5))+32
    return fahrenheit


degree_celcius = float(input("Degrees Celcius: "))
print(str(degree_celcius) + " degrees Celcius = " + str(celcius_fahrenheit(degree_celcius)) + " degrees Fahrenheit")
