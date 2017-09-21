# Define a class which has at least two methods:
# get_String: to get a string from console input
# print_String: to print the string in upper case.
# Hints: Use init method to construct some parameters

class Stringz:
    """
    This is a string class
    """

    def __init__(self, nr_cuv):
        self.nr_cuv = nr_cuv
        self.prop = ''

    def get_string(self):
        for i in range(self.nr_cuv):
            cuv = input('Introdu cuvant: ')
            self.prop += cuv + ' '

    def print_string(self):
        print(f'{self.prop.upper()[:-1]}.')

if __name__ == '__main__':
    propozitie = Stringz(5)
    propozitie.get_string()
    propozitie.print_string()
