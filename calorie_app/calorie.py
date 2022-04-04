

class Calorie:
    """calculates a persons calories requirements from the 
    parameters inputted"""

    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = temperature


    def calculate(self): 
        return(10*self.weight + 6.25*self.height - self.age + 5 - self.temperature*10)

