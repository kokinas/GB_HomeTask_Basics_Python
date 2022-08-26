class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'The car {self.name} went')

    def stop(self):
        print(f'The car {self.name} stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'The car {self.name} terned towards {direction} ')

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print(f"{self.name}'s speed is {self.speed}. Over speed!!!!")
        else:
            print(f"{self.name}'s speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            print(f"{self.name}'s speed is {self.speed}. Over speed!!!!")
        else:
            print(f"{self.name}'s speed is {self.speed}")


class SportCar(Car):
    def __init__(self):
        self.speed = 280


class PoliceCar(Car):
    def __init__(self):
        self.speed = 180
        self.color = 'blue'
        self.name = "LADA"
        self.is_police = True


car_1C = Car(85, 'Blue', "LADA", False)
car_1C.go()
car_1C.stop()
car_1C.turn('hospital')
car_2C = Car(180, 'green', 'BMW', False)
car_2C.stop()
car_2C.show_speed()
print(car_1C.direction)
car_3P = PoliceCar()
print(car_3P.is_police)
car_4S = SportCar()
print(car_4S.speed)
car_5T = TownCar(70, 'white', 'NIVA', False)

car_1C.show_speed()
car_5T.show_speed(55)
car_5T.show_speed(95)

"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

добавьте в базовый класс метод show_speed, который должен показывать текущую
 скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении
 скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о 
 превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ 
к атрибутам, выведите результат. Вызовите методы и покажите результат."""
