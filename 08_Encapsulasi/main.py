class Hero:

    # Encapsulation is to make all instances variables and class variabels private
    def __init__(self,name: str, health: int):
        self.__name = name
        self.__health = health

    # Creating a getter method.getter is used to "get" the private attributes and class variable
    def getHealth(self):
        return self.__health
    
    # Creating a setter method.a setter method is used to "set" or "change" the previous attributes value to the newest one
    def healthUp(self,totalHealthUp: int):
        self.__health += totalHealthUp
        return self.__health

    

gerry = Hero("Gerry",100)

# Get the instance health private variabel
print(f"Get the instance health private variabel: {gerry.getHealth()}")

# Set the current private instance variabel to the newer one
gerry.healthUp(10)
print(f"Total health after being changed: {gerry.getHealth()}")