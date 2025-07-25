class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print(f'{self.width*self.height}-площадь прямоугольника')
    def perimeter(self):
        print(f'{2*(self.width+self.height)}-периметр прямоугольника')
# Список размеров
rects = [(10, 5), (1, 4), (5, 6)]
print(f'{rects}-Список размеров\n')
# Проходим по списку и создаём объекты
for w, h in rects:
    r = rectangle(w, h)
    r.area()
    r.perimeter()
    print()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(f'{self.a+self.b}-результат сложения')
    def multiplication(self):
        print(f'{self.a*self.b}-результат умножения')
    def division(self):
        print(f'{self.a/self.b}-результат деления')
    def subtraction(self):
        print(f'{self.a-self.b}-результат вычитания')
test=Math(10,2)
test.addition()
test.multiplication()
test.division()
test.subtraction()

class site:

    type: str ='Кнопка'

    def __init__(self,text,loc=''):
        self.loc=loc
        self.text = text

    def click(self):
        print(f'Клик по кнопке {self.text}')
# TextBox=site('TextBox')
# CheckBox=site('CheckBox')
# RadioButton=site('RadioButton')
# WebTables=site('WebTables')
# Buttons=site('Buttons')
# Links=site('Links')
# BrokenLinks=site('BrokenLinks')
# UplANDDown=site('UplANDDown')
# DynProp=site('DynProp')

button_texts = [
    "Text Box",
    "Check Box",
    "Radio Button",
    "Web Tables",
    "Buttons",
    "Links",
    "Broken Links - Images",
    "Upload and Download",
    "Dynamic Properties"
]
buttons = [site(text) for text in button_texts]
print("Тексты кнопок:")
for button in buttons:
    print(button.text)

# c. Вызов метода click для каждой кнопки
print("\nКлики по кнопкам:")
for button in buttons:
    button.click()