class Dog:
    __instance = None

    def __new__(cls, breed=None, age=None, color=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.breed = breed
            cls.__instance.age = age
            cls.__instance.color = color
        return cls.__instance

    def __init__(self, breed=None, age=None, color=None):
        if Dog.__instance is None:
            self.breed = breed
            self.age = age
            self.color = color
            Dog.__instance = self

    def __call__(self, breed=None, age=None, color=None):
        if breed is not None:
            self.breed = breed
        if age is not None:
            self.age = age
        if color is not None:
            self.color = color
        return self

    def look(self):
        print(f'Собака выглядит так: {self.breed}, {self.age}, {self.color}')


dog1 = Dog('Labrador', '3', 'black')
dog2 = Dog('Doberman', '2', 'black')

dog1.look()
dog2.look()

dog2('Doberman', '5', 'brown')
dog2.look()