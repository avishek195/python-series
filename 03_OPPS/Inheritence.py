# class employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def showdetails(self):
#         print(f"The employee name is {self.name} and id is {self.id}")

# class newem(employee):
#     def show_interns(self):
#         print(f"Inter id is{self.id} and name is {self.name}")

# e1 = employee("Avi",23)
# e2 = newem("neel",24)
# e2.showdetails()
# e2.show_interns()


class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def show_car(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battry_power):
        super().__init__(brand,model)
        self.battry_power = battry_power
    def show_details(self):
        return f"{self.brand} {self.model} {self.battry_power}"

car1 = Car("odi", "o1")
print(car1.show_car())  # Output: odi o1

car2 = ElectricCar("Tesla", "v8", "85MAH")
print(car2.show_details()) # Tesla v8 85MAH
