# def task_1(a: int =123,b:float=123.123,c:str='124',d:list=[1,'2',3],e:bool=True):
#     return type(a),type(b),type(c),type(d),type(e)
# print(task_1())

def task_1_2(a: int,b:float,c:str,d:list,e:bool):
    return type(a),type(b),type(c),type(d),type(e)
print(task_1_2(1,12.12,'12',[1,'2',4],True))

# def task_1_3(a: int, b: float, c: str, d: list, e: bool):
#     types = []
#     for value in locals().values():
#         types.append(type(value))
#     return types
#
# print(task_1_3(1, 12.12, '12', [1, '2', 4], True))


def task_2()->list:
    a=[1,2,3,5,8,13,21]
    return a[0:3]
print(task_2(),"список а - Ряд Фибоначчи")

def task_3() -> int:
    while True:
        a = input("Введите число, которое желаете возвести в квадрат: \n")
        try:
            num = int(a)
            return num ** 2
        except ValueError:
            print("Ошибка: введите корректное целое число!")

print(task_3(), '- Квадрат вашего числа')

