class Hero:
    # Creating class variable and shared among all instances/objects
    total_hero = 0

    def __init__(self, name: str, health: int, attackPower: int, armor: int) -> None:
        # Creating and set the instance variable.this instance variables are spesific to each objects
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

        # Increment everytime when an object is made
        Hero.total_hero += 1

    # Void method that doesn't return anything
    # 'self' refers to an instances/objects so that we can interact with the objects.like access the attributes or the methods
    def show(self) -> None:
        print(f"Hero's name: {self.name} Hero's health: {self.health} Hero's attack power: {self.attackPower} Hero's armor: {self.armor}")

    # A method with an arugment
    # 'self' refers to an instances/objects so that we can interact with the objects.like access the attributes or the methods
    def powerUp(self,amountOfPower: int) -> int:
        self.attackPower += amountOfPower
        return self.attackPower

    # A method with return
    # 'self' refers to an instances/objects so that we can interact with the objects.like access the attributes or the methods
    def checkHealth(self):
        return self.health
    
hero1 = Hero("Gerry",100,10,50)

hero1.show()
hero1.powerUp(30)
hero1.show()
print(hero1.checkHealth())