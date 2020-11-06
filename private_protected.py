
# parent class
class Cat:
    def __init__(self):
        self.name = "Fluffy"        # public attribute
        self._color = "orange"      # protected attribute
        self.__breed = "tabby"      # private attribute
        self.activity = "sleeping"  # public attribute

    def information(self):
        print("{}, the {} {} cat is currently {}.".format(self.name, \
                                                          self._color,\
                                                          self.__breed, \
                                                          self.activity))

if __name__ == "__main__":
    cat1 = Cat()          # Create object
    cat1.information()
    
