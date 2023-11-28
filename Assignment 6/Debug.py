class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department

class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length


    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    #create your own function! what do you want it to do?


def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Sally" , 8)
    print(newDog.name, newDog.age)

    #and what about a new employee
    newEmployee = Employee("Rob", 1600, "Accounting")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)

    #now create and print out a cake you make
    cake1 = Cake("chocolate", "vanilla")
    print( cake1.flavor, cake1.frosting)

    cake2 = Cake("red velvet", "cream cheese")
    print(cake2.flavor, cake2.frosting)


    #and now create another cake and print it out



    #create a cat!
    cat1 = Cat("Kiko", 3, "long")
    print(cat1.name, cat1.age, cat1.fur_length)

    cat2 = Cat("Maria", 8, "short")
    print(cat2.name, cat2.age, cat2.fur_length)
    #create another cat!

    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())

    #create a car!
    car1 = Car("SUV", 2023, "Black" )
    print(car1.model, car1.year, car1.color)

    #Now print out the function you made for car :)

main()