
# def greet(fn):
#     def next():
#         print("This is a next func")
#         fn()
#     return next
# @greet
# def meet():
#     print("Hello, how are you?") 
#     print("Hello Edur. tumi kemon acho??")

# meet()


def deco(func):
    def wrapper(*args, **kwargs):
        fun_details = ",".join(str(arg) for arg in args)
        fun_details2 = ",".join(str(kw) for kw in kwargs)
        print(f"Function {func.__name__} is called with arguments {fun_details} and keyword arguments {fun_details2}")
        return func(*args, **kwargs)
    return wrapper
              



@deco
def myfun(name,roll = 56):
    print(f"Hello {name} your roll is {roll}")

myfun("Avishek")