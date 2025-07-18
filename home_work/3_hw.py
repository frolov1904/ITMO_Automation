import random
print("Задание №1\n")
def task1():
    x=random.randint(0,10)
    y=random.randint(0,10)
    print(x,'-первое число',y,'-второе число')
    if x>y:
        print(x,"-наибольшее\n")
    elif y>x:
        print(y,'-наибольшее\n')
    else:
        print('Числа равны\n')
task1()

print("Задание №2\n")
def task2():
    x=random.randint(-135,135)
    y=random.randint(-500,500)
    print(x,'-первое число',y,'-второе число')
    if abs(x-y)>=135:
        print('yes\n')
    else:
        print('no\n')
task2()

print("Задание №3\n")
def task3():
    x=random.randint(1,12)
    print(x,'-номер месяца')
    if x==12 or x<3:
        print('Зимa\n')
    elif x in range(3,6):
        print('Весна\n')
    elif 8>=x>=6:
        print("Летo\n")
    else:
        print('Осень\n')
task3()

print("Задание №4\n")
def task4():
    x=random.randint(0,100)
    y = random.randint(0, 100)
    z = random.randint(0, 100)
    print(x,y,z,'-числа')
    if x>10 and y>10 and z>10:
        print('yes\n')
    else:
        print('no\n')
task4()

print("Задание №5\n")
def task5():
    list=[]
    i=0
    count=0
    for i in range(5):
        x=random.randint(-10,10)
        list.append(x)
        i+=1
    print(list,'-список')
    for elem in list:
        if elem>0:
            count+=1
    print(count,'- кол-во положительных чисел\n')
task5()
print("Задание №6\n")
def task6():
    years = random.randint(0, 100)
    months = random.randint(1, 12)
    total_days = (12 * years + months) * 29

    print(f"Возраст:      {years} лет {months} месяцев")
    print(f"Всего дней:   {total_days} дней (по 29 дней в месяце)")

task6()
