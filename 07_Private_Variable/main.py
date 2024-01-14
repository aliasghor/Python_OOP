class Hero:
    # Creating a public class variable
    totalHero = 0

    # Creating a private class variable
    __total = 0

    def __init__(self,name: str, health: int) -> None:
        # Creating a public instance variables
        self.name = name
        self.health = health

        # Creating a private instance variable
        self.__private = "private"

        # Creating a procted instance variable
        self._protected = "protected"

# Instancied the objects
hero1 = Hero("hero1",100)
hero2 = Hero("hero2",50)

# Accessing the public instance variables
print("Accessing the public instance variable")
print(f"Accessed hero's 1 name = {hero1.name}")
print(f"Accessed hero's 1 health = {hero1.health}")

print(f"A hero's 2 name = {hero2.name}")
print(f"Accessed hero's 2 health = {hero2.health}")
print(f"Printed out the hero's 1 dictionary = {hero1.__dict__}")
print(f"Printed out the hero's 2 dictionary = {hero2.__dict__}")

# Accessing the private instance variables
print("\nAccessing the private instance variable")
print(f"Printed out the hero's 1 dictionary again = {hero1.__dict__}")
# print(f"Accessed the private instance variable = {hero1.__private}") if we accessed the private instance variable like this,this will not work
print(f"Accessed the private instance variable = {hero1._Hero__private}") # <- if we accessed the private instance variable like this,this will work

# Changing the private instance variable value
print("\nChanging the private instance variable value")
# Incorrect: hero1.__private = "Not private"
# This would create a new instance variable, not modifying the private one
# Correct: hero1._Hero__private = "Changing the _Hero__private instance variable value"
hero1._Hero__private = "Changing the _Hero__private instance variable value"
print(f"Printed out the hero's 1 dictionary again = {hero1.__dict__}")

# Accessing the protected instance variables
print("\nAccessing the protected instance variable")
# Emphasize the importance of not accessing protected variables directly
print("Protected instance variables are meant for internal use. Avoid direct access.")
print(f"Accessed the protected instance variable through object 2 = {hero2._protected}")

# Changing the protected instance variable value
print("\nChanging the protected instance variable value")
print(f"Printed out the hero's 2 dictionary = {hero2.__dict__}")
# Use a more explicit message about changing the protected variable
hero2._protected = "Changing the protected value through object 2"
print(f"Printed out the hero's 2 dictionary = {hero2.__dict__}")


print(f"Printed out the hero's 2 dictionary = {hero2.__dict__}")
hero2._protected = "Changing the protected value through object 2"
print(f"Printed out the hero's 2 dictionary = {hero2.__dict__}")

# Accessing the public and private class variables
print("\nAccessing the public and private class variables")
print(f"Printed out the class Hero dictionary = {Hero.__dict__}")
print(f"Accessed the public class variable = {Hero.totalHero}")
# print(f"Accessed the public class variable = {Hero.__total}")
# print(f"Accessed the private class variable = {_Hero__total}")

"""
    So in summary private instance variables it is not really that "private" you can still acess the private instance variable as long as you do it like _ClassName__thePrivateInstanceVariable.whereas a private class variable cannot be accessed regardless if we do it like _ClassName__thePrivateClassVariable

    protected instance variable it is the same like public we can accessed it outside the class and can change the proctected instance variable too.but it is important to note that whenever we see protected instance variable we shouldn't accessed that protected variable.protected instance variable is just a hint to the interpreter and to the human it self to at least "please be smart that you shouldn't access that protected instance variable"
"""