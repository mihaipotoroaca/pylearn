class Fruit:
    """
    This is a fruit class
    """
    variable = 5
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def _gigi(self):
        print('this is private')

    def show(self):
        print(f'This fruit is {self.color} and is named {self.name}')
        self._gigi()

    @staticmethod
    def apb(a, b):
        return a + b


if __name__ == '__main__':

    plum = Fruit('Plum', 'purple')
    apple = Fruit('Apple', 'red')

    plum.show()
    apple.show()
    plum._gigi()
    print(apple.__dict__)
    print(Fruit.apb(2,4))
    print(apple.apb(4,5))







