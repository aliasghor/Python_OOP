"""
    An object orinted programming is a paradigm in programming where every variabels that you have crated is called an "object" or an "instance"

    and OOP(object orinted programming) is a paradigm where you relies on class and object

    a furthermore explaination about what is class an object

    - Class:
        A class is a blueprint for us to make "something" or to make an "object"
        let's say Human is consider as a blueprint because each person is unique

    - Object/Instance:
        An object/instance is a variabel that you have just made from a class
        and an object has 2 values.and those values are:
            - Attributes(Like names,age,salary etc)
            - Methods(Spesific purporses or Spesific Functionality.like a person gets a salary, a person wants to meet with someone etc)
"""

class Human:
    """Declaring a class without constructor"""
    pass

ali = Human()

# Set the attributes like names,age etc
ali.name = "Ali Ganteng"
ali.age = 20
ali.handsome = True

# Print out all of the attributes using dictionary dunder or magic methods
print(ali.__dict__)

# Print the type of "ali"s object
print(type(ali))
print(ali) # <- or you can also do it like this