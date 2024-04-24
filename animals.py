class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("пение")

    def eat(self):
        print("Червяки")

class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def make_sound(self):
        print("рычание")

    def eat(self):
        print("Животные")

class Reptile(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("свист")

    def eat(self):
        print("Растения")

def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.personal = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_personal(self, personal):
        self.personal.append(personal)
        print(f"Сотрудник {personal} добавлен в зоопарк")

class ZooKeeper:
    def feed_animals(self, animal):
        print(f"Сотрудник кормит - {animal.name}")

class Veterinar:
    def heal_animals(self, animal):
        print(f"Ветеринар лечит -{animal.name}")

# Пример

bird = Bird("Воробей", 1, 25)
mammal = Mammal("Кот", 2, 5)
reptile = Reptile("Крокодил", 3, "зеленый")

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zookeeper = ZooKeeper()
veterinar = Veterinar()

zoo.add_personal(zookeeper)
zoo.add_personal(veterinar)

animal_sounds(zoo.animals)

zookeeper.feed_animals(bird)
veterinar.heal_animals(reptile)
