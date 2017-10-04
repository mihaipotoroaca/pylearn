from homework.new_coffee.coffee import Coffee


class CoffeeLatte(Coffee):

    """
    Coffee class with a bit of milk
    """

    def __init__ (self, latte_spoons, latte_sugar, latte_water, milk):
        super().__init__(coffee_spoons=latte_spoons, sugar=latte_sugar, water=latte_water)
        self.milk = milk

    def prepare_coffee(self):
        return Coffee.quantity + self.milk

    def prepare_time_coffee(self):
        time_to_prepare = self.water/10 + (self.coffee_spoons*10 + self.sugar*5)/5 + self.milk/10
        print(f'This coffe latte takes about {time_to_prepare} seconds to prepare')
    def energy(self):
        energy_level = self.milk * Coffee.quantity**2
        print(f'This Coffe Latte just raised your energy level with {energy_level}%')

if __name__ == '__main__':
    first_latte = CoffeeLatte(2,1,30,20)
    first_latte.prepare_time_coffee()
    first_latte.energy()
