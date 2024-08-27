class Car:
    def __init__(self, brand, model,prize):
        self.brand = brand
        self.model = model
        self.__prize = prize # Private variable

    def get_prize(self):
        return f"Rs. {self.__prize}"
    def set_prize(self, new_prize):
        self.__prize = new_prize
        return f"Rs. {self.__prize}" 
    def show_details(self):
        return f"{self.brand} {self.model}"

car1 = Car("abc", "V8", 12000)
# print(car1.__prize) # error

car1.brand = "abcd"
car1.set_prize(2300000)


print(car1.get_prize())
print(car1.brand)
print(car1.model)