# myfun = lambda : print("Hello") # Lambda function(Anonomus function)

# myfun()


# map
# l1 = [2,3,56,6,7,8,8]

# map1 = list(map(lambda x: x+2,l1))

# print(map1)



# filter
# l2 = [2,3,56,6,7,8,8]

# filter1 = list(filter(lambda x: x<=8,l2))

# print(filter1)



# reduce
l3 = [2,3,56,6,7,8,8]

reduce1 = functiontool.reduce(lambda x,y: x+y,l3)

print(reduce1)