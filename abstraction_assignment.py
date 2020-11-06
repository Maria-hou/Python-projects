from abc import ABC, abstractmethod

# parent class
class Numbers(ABC):
    def add(self, x, y):
        z = x + y
        print("\n{} + {} = {}".format(x, y, z))

    # this function is hidden 
    @abstractmethod
    def task(self, x, y):
        print("You entered {} and {}.".format(x, y))

# child class
class Multiply(Numbers):
    def task(self, x, y):
        z = x * y
        print("\n{} * {} = {}".format(x, y, z))

# another child class       
class Subtract(Numbers):
    def task(self, x, y):
        z = x - y
        print("\n{} - {} = {}".format(x, y, z))


if __name__ == "__main__":
    # object of the Multiply class created
    obj = Multiply()
    obj.task(4,5)
    obj.add(4,5)

    # object of the Subtract class created
    obj2 = Subtract()
    obj2.task(10,2)
    obj2.add(10,2)
