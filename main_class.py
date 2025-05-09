class car:
    def __init__(self, color, model, year):
        self.color = color  #instance variable
        self.model = model
        self.year = year 
        
    def start(self):
        return f"{self.model} is starting"
    
    def stop(self):
        return f"{self.model} is stoping"
            
myCar =  car("black","Honda","1999")
mycar2 = car("red","toyata","2000") 
mycar3 = car("orange","E-car","2000") 

print(myCar.color)
print(mycar3.start())

# -------------------------------------------------------------------------------------------------------------------------

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        
    def calculate_area(self):
        return self.length*self.width
    
rectangle = Rectangle(10,5)
area = rectangle.calculate_area()
print(area)


#---------------------------------------------------------------------------------------------------------------------------

class dog:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        
    def bark(self):
        return f"{self.name} says wolf"
    
my_dog =  dog("Buddy","Golden Retriever")
print(my_dog.bark())


#-----------------------------------------------------------------------------------------------------------------------------

class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius ** 2
    
my_circle = circle(5)
print("Area:",my_circle.area())


#------------------------------------------------------------------------------------------------------------------------------

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def description(self):
        return f"This car is a {self.brand} {self.model}"
    
My_car =  Car("Toyato","Corolla")
My_car1 = Car("Honda","old model")
print(My_car.description())
print(My_car1.description())


#-------------------------------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author
        
    def details(self):
        return f"'{self.title}' by {self.author}"
    
my_book = Book("1999","George Orwell")
author_book = Book("Untitled")

print(my_book.details())
print(author_book.details())

#-------------------------------------------------------------------------------------------------------------------------------

class CAR:
    def __init__(self, model, year):
        self.model = model 
        self.year = year
        
MY_CAR = CAR("toyato","1990")
MY_CAR.model = "HONDA"
print(MY_CAR.model)

MY_CAR.year = "2010"
print(MY_CAR.year)

#-------------------------------------------------------------------------------------------------------------------------------


class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def introduce(self):
        return f"My Name is {self.name} and I am in grade {self.grade}"
        
student1 = student("Alice","10th")
student2 = student("Bob", "12th")

print(student1.introduce())
print(student2.introduce())
        
#----------------------------------------------------------------------------------------------------------------------------------

class dog:
    species = "canis familiaris"        #instance variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = dog("milo", 3)
dog2 = dog("Buddy", 5)
print(dog1.name)
print(dog2.age)
print(dog2.species)

#-----------------------------------------------------------------------------------------------------------------------------------

class car:
    wheels = 4      #class variable
    
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        
car1 = car("Toyato","Camry")
car2 = car("Hondo","Accord")

car1.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(car.wheels)

#------------------------------------------------------------------------------------------------------------------------------------


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return f"New balance: {self.balance}"
        
account = BankAccount("Shriram",2000)
print(account.deposit(300))


#----------------------------------------------------------------------------------------------------------------------------------
# @classmethod

class person:
    _count = 0
    
    def __init__(self, name):
        self.name = name
        person._count += 1
        
    @classmethod
    
    def get_count(cls):
        return cls._count
    
p1 = person("jemail")
p2 = person("Nimra")
print((person.get_count()))


#----------------------------------------------------------------------------------------------------------------------------------


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    @classmethod
    def fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
temp = Temperature.fahrenheit(98.6)
print(temp.celsius)

#-----------------------------------------------------------------------------------------------------------------------------------

# @staticmethod

class mathUtils:
    @staticmethod
    
    def add(x,y):
        return x+y
    
total = mathUtils.add(71,33)
print(total)

#------------------------------------------------------------------------------------------------------------------------------------

class TemperatureConverter:
    @staticmethod
    
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/2) + 32
    
result = TemperatureConverter.celsius_to_fahrenheit(20)
print(result)


#------------------------------------------------------------------------------------------------------------------------------------

# overloading
class math:
    
    def Add(self, a, b=0 , c=0):
        return a+b+c

math1 = math()

print(math1.Add(2))
print(math1.Add(2,5))
print(math1.Add(2,5,9))

#--------------------------------------------------------------------------------------------------------------------------------------

class Animal:
    
    def sound(self):
        return "some genertic sound"
    
class dog(Animal):
    
    def sound(self):
        return "Bark"
    
class cat(Animal):
    
    def sound(self):
        return "Meow"
    
animals = [Animal() , dog(), cat()]

for animal in animals:
    print(animal.sound())
    
#------------------------------------------------------------------------------------------------------------------------------------

# inheritance
# This is chat GPT example
class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()    # Inherited from Animal
d.sleep()  # Inherited from Animal
d.bark()   # Defined in Dog

#-----------------------------------------------------------------------------------------------------------------------------------

# inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"
    
dog1 = Dog("Buddy")
print(dog1.speak())

# extra practice
anmal0 = Animal("something")
print(anmal0.speak())

#---------------------------------------------------------------------------------------------------------------------------------

# single-inheritance 

class vehicle:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def description(self):
        return f"{self.brand}{self.model}"
    
class car(vehicle):
    
    def wheels(self):
        return 4
    
mycars = car("Toyato","Corolla")
print(mycars.description())
print(mycars.wheels())

# multiple-inheritance

class Engine:
    def engine_type(self):
        return "v8"
    
class Transmission:
    def transmission_type(self):
        return "Automatice"
    
class SportsCar(Engine,Transmission):
    def car_type(self):
        return "Sports car"
    
my_sports_car =  SportsCar()

print(my_sports_car.engine_type())
print(my_sports_car.transmission_type())
print(my_sports_car.car_type())

#-------------------------------------------------------------------------------------------------------------------------------

class A:
    def greet(self):
        return "Hello from A"
    
class B(A):
    pass

class C(B):
    pass

obj = C()
print(obj.greet())
print(C.__mro__)    #Method Resolution Order (MRO)

#----------------------------------------------------------------------------------------------------------------------------------

class X:
    def greet(self):
        return "Hello from X"
    
class Y:
    def greet(self):
        return "Hello from Y"
    
class Z(X,Y):
    pass

obj = Z()
print(obj.greet())
print(Z.__mro__)    #Method Resolution Order (MRO)

#-----------------------------------------------------------------------------------------------------------------------------------

# Polymorphism

class Bird:
    def fly(self):
        return "Bird is flying"
    
class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"
    
class Ostrich(Bird):
    def fly(self):
        return "Ostrich is flying"
    
def make_fly(bird):
    print(bird.fly())
    
bird1 = Sparrow()
bird2 = Ostrich()

make_fly(bird1)
make_fly(bird2)

#

class Animal:
    def sound(self):
        return "some generic animal sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
def make_sound(animal):
    print(animal.sound())
    
aniaml1 = Dog()
animal2 = Cat()

make_sound(aniaml1)
make_sound(animal2)

# --------------------------------------------------------------------------------------------------------------------------------

# Encapsulation
# Encapsulation = Hiding internal data and controlling access through methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount(20000)
account.deposit(5000)
account.withdraw(7000)

print(account.get_balance())

#---------------------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, name ,salary):
        self.name = name
        self._salary = salary       #protected
        
    def display(self):
        return f"Name:{self.name}, Salary:{self._salary}"
    

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department =  department
        
    def display_Manager(self):
        return f"Name:{self.name}, Department:{self.department}, Salary:{self._salary}"
    
emp = Employee("John",50000)
mag = Manager("Alice", 80000, "HR")

print(emp.display())
print(mag.display_Manager())

#------------------------------------------------------------------------------------------------------------------------------------

#abstractmethod

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        
    def area(self):
        return self.width*self.heigth
    
    def perimeter(self):
        return 2*(self.heigth + self.width)
    
rect = Rectangle(5,10)

print(f"area of rectangle: {rect.area()}")
print(f"perimeter of rectangle: {rect.perimeter()}")

#------------------------------------------------------------------------------------------------------------------

class bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    def deposited(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposited: {amount}, New_balance: {self.__balance}")
        
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"withdraw: {amount}, New_balance: {self.__balance}")
        else:
            print("Insufficient Function Invalid Amount")
            
    def get_balance(self):
        return self.__balance
    
account = bankaccount("junny", 50000)
account.deposited(30000)
account.withdraw(20000)
print(account.get_balance())

#------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name = name
        
    @abstractmethod
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self,name, salary):
        super().__init__(name)
        self.salary = salary
        
    def calculate_salary(self):
        return self.salary
    
emp1 = FullTimeEmployee("Bobby",80000)
print(f"salary of {emp1.name}: {emp1.calculate_salary()}")

#----------------------------------------------------------------------------------------------------------------


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
book = Book(1984,"Georage orwell")
print(book)

#---------------------------------------------------------------------------------------------------------------

# advanced OOP concept 

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)       
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = vector(2,3)
v2 = vector(4,5)

v3 = v1+v2

print(v3)

#----------------------------------------------------------------------------------------------------------------

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = self.start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1
        
countdown = Countdown(5)
for i in countdown:
    print(i)
    
#-----------------------------------------------------------------------------------------------------------------

# fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a,b = b,a + b
        
fib = fibonacci(7)
for i in fib:
    print(i)
    
#----------------------------------------------------------------------------------------------------------------

class Engine:
    def start(self):
        return "Engine Starts."
    
class car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
    def start(self):
        return f"{self.model}: {self.engine.start()}"
    
car0 = car("Toyata")
print(car0.start())

#------------------------------------------------------------------------------------------------------------------

