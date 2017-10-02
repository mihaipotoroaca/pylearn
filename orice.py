from homework.latte_machiato.coffee_latte import CoffeeLatte
from homework.new_coffee.coffee import Coffee

if __name__ == '__main__':
    first_latte = CoffeeLatte(2,1,30,20)
    first_latte.prepare_time_coffee()
    first_latte.energy()
    first_coffee = Coffee(2,2,40)
    second_coffee = Coffee(3,1,20)

    first_coffee.prepare_coffee()
    first_coffee.show_coffee_preparation()
    first_coffee.prepare_time_coffee()

    second_coffee.prepare_coffee()
    second_coffee.show_coffee_preparation()
    second_coffee.prepare_time_coffee()