class People:
    def __init__(self, name=None):
        self.name = name
        self.index = 0

    def __next__(self):
        if self.index < len(self.name):
            person = self.name[self.index]
            self.index += 1
            return person
        else:
            raise StopIteration


    def add_person(self, person):
        self.name.append(person)

    def __iter__(self):
        self.index = 0
        return self

people_list = People(['Alexander', 'Ivan', 'Olga'])
people_list.add_person(input())

for person in people_list:
    print(person)
    