# x =10

# def show():
#     global x
#     x=x+10
#     print(x)
#     print(f"Value of local x is {x}")
# print(f"value of global x is {x}")

# show()
# print(f"value of global x is {x}")



x =10

def show():
    global x
    x=10
    print(x)
    print(f"Value of local x is {x}")
    return x
print(f"value of global x is {x}")

x+=show()
print(f"value of global x is {x}")



