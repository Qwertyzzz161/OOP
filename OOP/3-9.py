#Задание 3.Создайте класс MeansOfTransport }}(для определения цвета и марки машины),
#принимающий 2 аргумента при инициализации (марка и цвет транспортного средства).
class MeansOfTransport:
    def __init__(self, color=None, brand=None):
        self.color = color
        self.brand = brand


#Задание 4.Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
    def set_color(self, color):
        self.color = color

    def set_brand(self, brand):
        self.brand = brand

    def get_color(self):
        return self.color

    def get_brand(self):
        return self.brand

# showcars = MeansOfTransport()
# showcars.set_color(input("Введите цвет "))
# showcars.set_brand(input("Введите марку "))
#
# print(f"Цвет транспортного средства -",showcars.get_color())
# print(f"Марка транспортного средства -",showcars.get_brand())


#Задание 5. Реализуйте два класса Car и Moped, которые
# будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес.
class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, color, brand, number_of_wheels=4, country=None, max_speed=None):
        super().__init__(color, brand)
        self.number_of_wheels = number_of_wheels
        self._country = country
        self.__max_speed = max_speed

    @classmethod
    def ShowCarDrive(cls):
        print(cls.car_drive)


    def __getattribute__(self, item):
        if item == 'model':
            raise ValueError("Нельзя выбрать модель")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'model':
            raise AttributeError("Недопустимый аттрибут")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)

    def __call__(self, *args, **kwargs):
        print("Функция теперь функтор")
        return self.color, self.brand

    def __repr__(self):
        return f"{self.__class__}: {self.color}, {self.brand}"

    def __str__(self):
        return f"{self.color},{self.brand}"

    def __hash__(self):
        return hash((self.color, self.brand))

    def __len__(self):
        return self.__max_speed

    def __bool__(self):
        return bool(self.__max_speed)


class Moped(MeansOfTransport):
    def __init__(self, color, brand, number_of_wheels=2):
        super().__init__(color, brand)
        self.number_of_wheels = number_of_wheels


#Задание 6. В классе {{Moped}}напишите статическую функцию,
# которая на вход будет принимать расстояние и максимальную скорость, а
# на выходе получать время, за которое проедет мопед это расстояние.
    @staticmethod
    def TimetoDistance(speed, distance):
        return distance / speed

# distance = int(input("Введите расстояние в километрах: "))
# speed = int(input("Введите скорость в км/ч: "))
#
# time = Moped.TimetoDistance(speed, distance)
# print(f'Время за которое будет преодолено расстояние {distance} = {time} часов')



#Задание 7. Попробуйте инициализировать несколько любых переменных в классе Car и
# сделайте одну переменную приватной, одну защищенной.
# Попробуйте получить к ним доступ. Какой результат?
# - Доступ к переменной _country осуществляется без проблем, так как она защищенная
# - Доступ к переменной __max_speed не доступен, она приватна. Доступ только внутри класса.

# showcountry = Car("blue","Toyota", "4", "Japan", "260")
# print(showcountry._country)
# print(showcountry.__max_speed)




# Задание 8. В классе Car добавьте переменную класса car_drive = 4
# и реализуйте classmethod, который выводит на экран переменную car_drive

#drive = Car.ShowCarDrive()



#Задание 9. Реализуйте все возможные магические методы в классе Car
test = Car("black",  "Audi" ,"4", "Germany", 240)
# test.model = red #  __setattr__ - работает, когда пытаемся изменить аттрибут

# t = test.model #  __getattribute__ - работает при доступе к любому аттрибуту

# print(test.asd) #  __getattr__ - работает при доступе не несоществующему аттрибуту

# print(test.__dict__)
# del test.brand # __delattr__ - работает при удалении аттрибута
# print(test.__dict__)


# c = Car("white", "Lexus") # __call__ - позволяет использовать класс как функцию
# c()


# test # __repr__ - изменяет отображение информации в режиме отладки


# print(test) # __str__ - изменяет отображение информации для пользователя

# test1 = Car("black","Audi") # __hash__ - используется для работы с изменяемыми обьектами
# print(hash(test), hash(test1))


# print(len(test)) # __len__ - используется для определения длины обьекта
# print(bool(test)) # __bool__ - используется для определения значения обьекта в виде True/False

