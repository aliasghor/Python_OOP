class Hero:
    """
        Creating a class with a constructor __init__() method
        constructor is a method that will be executed first
        everytime that we make an object/instance.and the
        process of creating an object/instance also known
        as instancied
    """
    def __init__(self,name):
        """
            self refers to an object that we've just made
            so without a self keyword this __init__() method
            cannot be executed.so self keyword is a must
            everytime when we want to interact with an object
            or to set the attributes for an objects

            self.name = name
            means that we are going to create an attribute called name
            and that attribute is assigned to a parameter called name
            note that self.name and name are a two different things

        """
        self.name = name

        print(f"Creating a hero called: {self.name}")
        print(f"self has a memory address of: {hex(id(self))}")

hero1 = Hero("Gerry")
hero2 = Hero("Ali Ganteng")

# as you can see these 2 print function returns the same memory address like on the __init__() method
print(f"\nExplicitly write the memory address outside the __init__() method: {hex(id(hero1))}")
print(f"Explicitly write the memory address outside the __init__() method: {hex(id(hero2))}")