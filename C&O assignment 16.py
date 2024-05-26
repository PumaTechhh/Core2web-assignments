
# 1. Create a Class Human with instance attributes and methods

class Human:
    def __init__(self, name, age):
        print("In Demo Constructor")
        self.name = name
        self.age = age
    
    def information(self):
        print("Name is:", self.name)
        print("Age is:", self.age)

name = input("Enter name: ")
age = int(input("Enter age: "))

if __name__ == "__main__":
    obj1 = Human(name, age)
    obj1.information()

# 2. Create a Vehicle class with methods and child class that overrides methods

class Vehicle:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        self.speed += 5
        print(f"Speed is now: {self.speed}")
    
    def brake(self):
        self.speed -= 5
        print(f"Speed is now: {self.speed}")
    
    def honk(self):
        print("Honk! Honk!")

class Car(Vehicle):
    def accelerate(self):
        self.speed += 10
        print(f"Car speed is now: {self.speed}")
    
    def honk(self):
        print("Car horn: Beep! Beep!")

vehicle = Vehicle("Toyota", "Camry", 2020, 60)
car = Car("Honda", "Civic", 2022, 70)

vehicle.accelerate()
vehicle.honk()
car.accelerate()
car.honk()

# 3. Create Parent class with classmethod, staticmethod, and instance method

class Parent:
    @classmethod
    def class_method(cls):
        print("This is a class method")
    
    @staticmethod
    def static_method():
        print("This is a static method")
    
    def instance_method(self):
        print("This is an instance method")

class Child(Parent):
    pass

child = Child()
child.class_method()
child.static_method()
child.instance_method()

# 4. Create parent class and override method in child class

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

child = Child()
child.show()

# 5. Real-time example of Cricket that describes inheritance

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def play(self):
        print(f"{self.name} is playing as {self.role}")

class Batsman(Player):
    def __init__(self, name):
        super().__init__(name, "Batsman")
    
    def play(self):
        print(f"{self.name} is batting")

class Bowler(Player):
    def __init__(self, name):
        super().__init__(name, "Bowler")
    
    def play(self):
        print(f"{self.name} is bowling")

player1 = Batsman("Sachin")
player2 = Bowler("Warne")

player1.play()
player2.play()

# 6. WAP for MRO with flow diagram

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

print(E.mro())

# 7. Create class with destructor and demonstrate object deletion

class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")
    
    def __del__(self):
        print(f"{self.name} destroyed")

obj1 = Test("Object1")
obj2 = Test("Object2")
obj3 = obj1
del obj2


# 8. Draw flow diagram for given code

class Demo:
    def __init__(self):
        print("In Constructor")
    
    def __del__(self):
        print("In Destructor")

def Fun():
    print("In fun")
    obj = Demo()
    print("End fun")
    return obj

retObj = Fun()
print("End Code")

# 9. Real-time example for classes and objects with classmethod, staticmethod, and instance method

class Library:
    books_available = 0

    @classmethod
    def update_books(cls, count):
        cls.books_available += count
        print(f"Books available: {cls.books_available}")
    
    @staticmethod
    def library_info():
        print("Welcome to the library")
    
    def __init__(self, name):
        self.name = name
    
    def member_info(self):
        print(f"Member: {self.name}")

member = Library("John Doe")
member.library_info()
Library.update_books(5)
member.member_info()

# 10. Real-time example of inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Barks"

class Cat(Animal):
    def sound(self):
        return "Meows"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} {dog.sound()}")
print(f"{cat.name} {cat.sound()}")
