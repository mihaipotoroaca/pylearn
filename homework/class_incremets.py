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

class SmallCar(Car):
        def __init__(self, small_car_name, small_car_color, size):
            super().__init__(name=small_car_name, color=small_car_color)
            self.size = size

        def speed(self):
            return self.size*2

        def show_speed(self):
            print(f'This is the small car speed {self.speed()}km/h')


if __name__ == '__main__':

    Duster = Car('Dacia Duster', 'black')
    Sandero = Car('Dacia Sandero', 'red')
    polo = SmallCar('VW Polo', 'blue', 50)
    Duster.show()
    Sandero.show()
    Duster.ShowNrOfInst()
    Car.ShowNrOfInst()
    polo.show()
    polo.show_speed()




