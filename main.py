import pickle
class Animal (object):
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def make_sound(self):
        return f"{self.name} says {self.sound}"
    def eat(self):
        return f"{self.name} eats {self.food}"

class Bird(Animal):
    def __init__(self, name, age, food, sound):
        super().__init__(name, age)
        self.food = food
        self.sound = sound

    def make_sound(self):
        return f"{self.name} говорит {self.sound}"
    def eat(self):
        return f"{self.name} кушает {self.food}"

class Mammal(Animal):
    def __init__(self, name, age, food, sound):
        super().__init__(name, age)
        self.food = food
        self.sound = sound

    def make_sound(self):
        return f"{self.name} говорит {self.sound}"
    def eat(self):
        return f"{self.name} кушает {self.food}"

class Reptile(Animal):
    def __init__(self, name, age, food, sound):
        super().__init__(name, age)
        self.food = food
        self.sound = sound

    def make_sound(self):
        return f"{self.name} говорит {self.sound}"
    def eat(self):
        return f"{self.name} кушает {self.food}"

class Zoo_keeper():
    def __init__(self, name, age, experience, salary):
       self.name = name
       self.age = age
       self.experience = experience
       self.salary = salary

    def feed_animals(self, animal):
        print( f"{self.name} покормил {animal.name}")
class Veterinarian():
    def __init__(self, name, age, experience, education):
        self.name = name
        self.age = age
        self.experience = experience
        self.education = education
    def heal_animals(self, animal):
        print(f"{self.name} вылечил {animal.name}")

class Zoo():
    def __init__(self, name, address, animals, keepers, veterinarians):
        self.name = name
        self.address = address
        self.animals = []
        self.keepers = []
        self.veterinarians = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def add_keeper(self, keeper):
        self.keepers.append(keeper)
        print(f"Сотрудник {keeper.name} приписан к зоопарку {self.name}")
    def add_veterinarian(self, veterinarian):
        self.veterinarians.append(veterinarian)
        print(f"Сотрудник {veterinarian.name} приписан к зоопарку {self.name}")

    def save_zoo(self):
        with open('zoo_data.pkl', 'wb') as file:
            pickle.dump(self, file)

    def load_zoo():
        try:
            with open('zoo_data.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None


def animal_eat(animals):
    for animal in animals:
        print (animal.eat())
def animal_make_sound(animals):
    for animal in animals:
        print (animal.make_sound())

zoo1 = Zoo.load_zoo()
# zoo_list = []
# zoo_keepers = []
# veterinarians = []
# zookeeper1 = Zoo_keeper("Саша", 30, 5, 10000)
# veterinarian1 = Veterinarian("Витя", 25, 3, "Высшее")
# zoo1 = Zoo("Зоопарк", "Москва", zoo_list, zoo_keepers, veterinarians)
# zoo_list.append(Bird("Ворона", 5, "Всё", "Кар-кар"))
# zoo_list.append(Mammal("Корова", 5, "Трава", "Му"))
# zoo_list.append(Reptile("Кобра", 5, "Мыши", "Ш-ш-ш"))
# zoo1.add_animal(zoo_list[0])
# zoo1.add_animal(zoo_list[1])
# zoo1.add_animal(zoo_list[2])
# zoo1.add_keeper(zookeeper1)
# zoo1.add_veterinarian(veterinarian1)

animal_eat(zoo1.animals)
animal_make_sound(zoo1.animals)

zoo1.veterinarians[0].heal_animals(zoo1.animals[0])
zoo1.keepers[0].feed_animals(zoo1.animals[0])
zoo1.save_zoo()