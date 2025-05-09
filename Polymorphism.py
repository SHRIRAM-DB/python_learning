class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  # Output: Woof!
make_animal_speak(Cat())  # Output: Meow!
