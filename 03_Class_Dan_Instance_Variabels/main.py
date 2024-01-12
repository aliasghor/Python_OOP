class Hero:
    """
        A variabel that is declared outside of an init method
        are also known as class variabel

        a class variabel is shared among all instances or object
        but a class variabel is only available on the class.and
        cannot be accessed through an object
    """
    total_of_hero = 0

    def __init__(self,name,attackPower):
        """
            These 2 variabels are also known as instance variabel
            instance variabels and attributes are basically the same

            instance variables is a variable that is declared inside
            of an __init__() method
            whereas attributes referes to an instance of that variables name
            

            and the purpose of instance variabel is to
            set the instance variabel to whatever the arguments are passed
        """
        self.name = name
        self.attackPower = attackPower

        Hero.total_of_hero += 1 # increment everytime when we make an object/instance

hero1 = Hero("Gerry",50)
print(f"hero1 has a name called {hero1.name} and has an attack power for about {hero1.attackPower}")
print(Hero.total_of_hero)

hero2 = Hero("Mogi",60)
print(f"hero2 has a name called {hero2.name} and has an attack power for about {hero2.attackPower}")
print(Hero.total_of_hero)

# Print out all of the attributes or instance variabels
print(hero1.__dict__)
print(hero2.__dict__)

# Print out all that is inside of a class
print(Hero.__dict__) # Note that the doc string will be also get printed out🥲