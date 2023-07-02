class tempConverter() :
    def FahrenheitToCelsius(self, Fahrenheit) :
        return (Fahrenheit - 32) * (5/9)

TC = tempConverter()
print( TC.FahrenheitToCelsius(78) )
