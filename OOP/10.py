class Calculator:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def sum(self):
        self.result = self.x + self.y

class CalculatorS(Calculator):
    def sum(self):
        self.result = str(self.x) + str(self.y)

summator = Calculator(5, 7)
summator.sum()
print(summator.result)

summators = CalculatorS(5, 7)
summators.sum()
print(summators.result)
