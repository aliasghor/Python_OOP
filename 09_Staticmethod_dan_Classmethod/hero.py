class Hero:
    # Creating a private class variabel.to keep track how many hero's or objects that are made
    __total = 0

    __company = 'Ubisoft'

    # Creating a constructor to initialize the attributes after we made an objects
    def __init__(self,name: str, health: int) -> None:
        # Creating a private instance variabel
        self.__name = name
        self.__health = health
        
        Hero.__total += 1

    # Creating a getter method to "get" the private instance variabels
    @property
    def getName(self):
        pass

    @getName.getter
    def getName(self):
        return self.__name
    
    @property
    def getHealth(self):
        pass

    @getHealth.getter
    def getHealth(self):
        return self.__health

    # Creating a static method.a static method is a method that only belongs to the class it self
    @staticmethod
    def isLow(currentHealth):
        """
            This method only belongs to the class and has a decorator called @staticmethod on
            the top of the method

            This method cannot access through an object nor to modify the attributes through
            this method nor accessing the class instance or instace private variabel it self
        """
        if currentHealth < 0:
            print("Error hero's health cannot be lower than zero!!")

    # Creating a class method.a class method is a method that only belongs to the class it self
    @classmethod
    def getTotal(cls):
        """
            This method only belongs to the class it self and has a decorator called @classmethod on the top of the method

            that means this method can has a privilege to access a class variabel and to modify every class variabel within this class
        """
        return cls.__total
    
    @classmethod
    def changeCompany(cls,newCompanysName):
        cls.__company = newCompanysName
        return cls.__company