class Animal():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def walk(self):
        return f"{self.name} is walking"

    def more_info(self):
        return f"{self.name} is {self.age} years old and its weight is {self.weight} t"

    def __str__(self):
        return f"name={self.name}, age={self.age}, weight={self.weight} t"


class Cow(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.moo = "MOooooo MOooooo"

    def cow(self):
        res = super().eat()
        return f"{self.moo}, {res}"

    def graze(self):
        return f"{self.name} is grazing in the field"


class Pig(Animal):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color
        self.hru = "Hruu Hruu"

    def pig(self):
        res = super().eat()
        return f"{self.hru}, {res}, and color is {self.color}"

    def roll_in_mud(self):
        return f"{self.name} is rolling in the mud"


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.mya = "Myauuuu myauuu"

    def myau(self):
        res = super().eat()
        return f"{self.mya}, {res}"

    def run(self):
        return f"{self.name} is running fast after a mouse"


cow = Cow("Bella", 5, 4)
pig = Pig("Peppa", 2, 1, "pink")
cat = Cat("Tom", 3, 0.05)

for animal in [cow, pig, cat]:
    print(animal)
    print(animal.eat())
    print(animal.sleep())
    print(animal.walk())
    print("---")

print(cow.cow())
print(cow.graze())
print(pig.pig())
print(pig.roll_in_mud())
print(cat.myau())
print(cat.run())