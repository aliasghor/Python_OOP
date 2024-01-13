class Hero:
    
    def __init__(self,name,health,attackPower,armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def attack(self,opponent):
        print(f"{self.name} attack {opponent.name}")
        opponent.underAttack(self,self.attackPower)
    

    def underAttack(self,opponent,totalAttack):
        print(f"{self.name} is under attacked by {opponent.name}")
        recevied_attack = totalAttack / self.armor
        print(f"{opponent.name} hit {self.name} for about: {recevied_attack} damage")
        self.health -= recevied_attack
        print(f"Health {self.name} after being attacked: {self.health}")