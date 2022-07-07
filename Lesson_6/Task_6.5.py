class Statinory():

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Statinory):

    def draw(self):
        print('Порисуем шариковой ручкой')


class Pencil(Statinory):

    def draw(self):
        print('Порисуем карандашиком')


class Handle(Statinory):

    def draw(self):
        print('Порисуем маркером')


pen_1 = Pen('Pen')
pen_1.draw()
pen_2 = Pen('Pen')
pen_2.draw()
Statinory_1 = Statinory('Some Statinory')
Statinory_1.draw()
pencil_1 = Pencil('Wooden pencil')
pencil_1.draw()
handle_1 = Handle('Handle')
handle_1.draw()
