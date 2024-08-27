class Car:
    def __init__(self, brand, model,prize):
        self.brand = brand
        self.__model = model
        self.__prize = prize # Private variable

    def get_prize(self):
        return f"Rs. {self.__prize}"
    def set_prize(self, new_prize):
        self.__prize = new_prize
        return f"Rs. {self.__prize}" 
    def show_details(self):
        return f"{self.brand} {self.__model}"
    @staticmethod
    def description(car):
        return f"This car is suprt fast and the prize is {car.__prize}"
    @property
    def model(self):
        return self.__model

car1 = Car("abc", "V8", 12000)
# print(car1.__prize) # error

car1.brand = "abcd"
# car1.model = "tess" # Error
car1.set_prize(2300000)
print(car1.description(car1))
print(car1.model)
# print(car1.model()) # Error