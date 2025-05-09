from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass  # No implementation here

# Concrete class
class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

# a = Animal()  # ❌ Error: Can't instantiate abstract class
d = Dog()
d.speak()  # ✅ Output: Bark
