"""
    Encapsulation is to make every variabels private
"""

class Hero:

    def __init__(self,name: str, health: int, attackPower: int):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # Getter.getter is used to get the private instance or class variabels
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getAttackPower(self):
        return self.__attackPower
    
    # Setter.setter is used to "set" the current attributes/instance variabels to the newest one.what i mean is that setter is used to change the previous private variable value to the new private variable value

    def healthUp(self,newHealthValue: int):
        self.__health += newHealthValue
        return self.__health
    
    def attack(self,opponentName: object ,totalDamage: int):
        print(f"{self.__name} attack {opponentName.__name}")
        opponentName.__health -= totalDamage
        return self.__health


gerry = Hero("Gerry",100,10)
mogi = Hero("Mogi",100,40)

gerry.attack(mogi,gerry.getAttackPower())
print(f"Mogi's health = {mogi.getHealth()}")

gerry.healthUp(10)
print(f"Gerry's new health = {gerry.getHealth()}")