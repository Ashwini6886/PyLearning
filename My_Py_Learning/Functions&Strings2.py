#class and method

class Person:
    def init(self,name):
        self.name=name
        print("Hello")

    def greet(self):
        print("Hello, my name is "+self.name)

person = Person("alice")
print(person.name)

person.greet()
