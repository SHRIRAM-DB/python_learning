# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Usage
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog
