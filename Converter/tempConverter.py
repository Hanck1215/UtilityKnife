import Package.CalculatorClass as CalcGenerator

class tempConverter() :
    Calc = None

    def __init__(self) :
        self.Calc = CalcGenerator.getCalculator()

    def FahrenheitToCelsius(self, Fahrenheit) :
        return self.Calc.sub(Fahrenheit, 32) * self.Calc.div(5, 9)
    
tc = tempConverter() 
print(tc.FahrenheitToCelsius(78))
    




