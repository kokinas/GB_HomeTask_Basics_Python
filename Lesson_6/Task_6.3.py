class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Possision(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


mr_pupkin = Possision('Vasiliy', 'Pupkin', 'accounter', 67500, 12500)
mr_pupkin.get_full_name()
mr_pupkin.get_total_income()
