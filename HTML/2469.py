def convertTemperature(celsius):
    kelvin = celsius + 273.15
    farhenheit = celsius * 1.80 + 32.00
    return [round(kelvin, 2), round(farhenheit, 2)]
