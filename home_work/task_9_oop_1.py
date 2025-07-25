from task_9_checks import Checks
class Car(Checks):
    def __init__(self, color='', type='', year=0, loc=''):
        super().__init__(loc) #класс родительский
        self.color=color
        self.type=type
        self.year=year
        self.loc=loc
    def start(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def set_year(self,year):
        self.year=year
    def set_type(self,type):
        self.type=type
    def set_color(self, color):
        self.color = color
# Примеры создания объектов и вызовов методов
car1 = Car('Красный','Седан',2020, 'Москва')
car2 = Car(color='Синий', type='Хэтчбек', year=2018, loc='Казань')
car3 = Car(loc='Новосибирск')  # без параметров

# Тестируем методы
car1.start()
car2.stop()

car3.set_color('Черный')
car3.set_type('Кроссовер')
car3.set_year(2024)

# Результат метода check_text() от каждого объекта
print(car1.check_text())  # Москва
print(car2.check_text())  # Казань
print(car3.check_text())  # Новосибирск
