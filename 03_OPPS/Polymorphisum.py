class Car:
    def __init__(self,name, brand):
      self.name = name
      self.brand = brand
    def fuel_type(self):
       return "petrol"
    
class Electric(Car):
    def __init__(self, name, brand, battery_capacity):
      super().__init__(name, brand)
      self.battery_capacity = battery_capacity
    def fuel_type(self):
       return "battry"

car1 = Car("oddi", "v8")
car2 = Electric("tesla", "v8", "20kw")

print(car1.fuel_type())
print(car2.fuel_type())
    