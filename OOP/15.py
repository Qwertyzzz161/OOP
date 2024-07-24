import logging

loggername = "Task15"
logger1 = logging.getLogger(loggername)
logger1.setLevel(logging.INFO)

handler1 = logging.FileHandler(f"{loggername}.log", mode='w')
formatter1 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler1.setFormatter(formatter1)
logger1.addHandler(handler1)

class Car:
    def __init__(self, color=None, brand=None, year=None):
        self._color = color
        self._brand = brand
        self._year = year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        old_color = self._color
        self._color = new_color
        logger1.info(f"Цвет изменился с {old_color} на {new_color}")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        old_brand = self._brand
        self._brand = new_brand
        logger1.info(f"Марка изменилась с {old_brand} на {new_brand}")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        old_year = self._year
        self._year = new_year
        logger1.info(f"Год изменился с {old_year} на {new_year}")



a = Car('blue','lada',2015)
a.color = 'silver'
a.brand = 'tesla'
a.year = 2024
