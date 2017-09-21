class Car:
    """
    This is a car class
    """
    nrOfInst = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Car.nrOfInst += 1

    def show(self):
        print(f'This is a {self.color} car and  is named {self.name}')
    @staticmethod
    def ShowNrOfInst():
        print(f'The class Car is instanced {Car.nrOfInst}')


if __name__ == '__main__':

    Duster = Car('Dacia Duster', 'black')
    Sandero = Car('Dacia Sandero', 'red')

    Duster.show()
    Sandero.show()
    Duster.ShowNrOfInst()
    Car.ShowNrOfInst()



