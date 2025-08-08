class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power = + 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance = - 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")


war1 = Warrior("Степа", 76, 54, "коричневый") # первый воин, в скобках параметры
print(war1) # <__main__.Warrior object at 0x000001D3F2C97CB0> краткая информация об обьекте

print(war1.name) # обратились к конкретному обьекту выдал: Степа

print(war1.endurance) #сила 54
war1.sleep()   # лег спать, силу увеличивается на 2
print(war1.endurance) #сила 56



