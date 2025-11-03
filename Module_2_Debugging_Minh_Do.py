##Minh Do
##CIS 256
##
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound.")


class Dog(Animal):
    def __init__(self, name, breed):#missing name 
        super().__init__(name) # Calls Animal.__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")


# Create a Dog object
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()