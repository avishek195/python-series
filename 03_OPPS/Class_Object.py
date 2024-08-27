class Person:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def view(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


newperson = Person("Avishek", 24)
newperson.view()