class Coffee:
    """
    Coffee class with prepared coffee quantity and time
    """
    def __init__(self, coffee_spoons, sugar, water):
        self.coffee_spoons = coffee_spoons
        self. sugar = sugar
        self.water = water
    quantity = 0
    def prepare_coffee(self):
        Coffee.quantity = (self.coffee_spoons*10 + self.sugar*5)/10 + self.water
        return Coffee.quantity

    def show_coffee_preparation(self):
        print(f'This coffee is {Coffee.quantity} ml. '
              f'It consists of {self.coffee_spoons} coffee spoons, '
              f'this means {self.coffee_spoons*10} grams of coffe, '
              f'{self.sugar} sugar cubes, '
              f'this means {self.sugar*5} grams of sugar '
              f'and {self.water} ml of hot water')

    def prepare_time_coffee(self):
        time_to_prepare = self.water/10 + (self.coffee_spoons*10 + self.sugar*5)/5
        print(f'This coffe takes about {time_to_prepare} seconds to prepare')


if __name__ == '__main__':

    first_coffee = Coffee(2,2,40)
    second_coffee = Coffee(3,1,20)

    first_coffee.prepare_coffee()
    first_coffee.show_coffee_preparation()
    first_coffee.prepare_time_coffee()

    second_coffee.prepare_coffee()
    second_coffee.show_coffee_preparation()
    second_coffee.prepare_time_coffee()