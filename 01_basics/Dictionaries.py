mydic = {
    "id": 212,
    "name": "Avishek",
    "roll": 45
}

# print(mydic["id"]) #212
# print(mydic.get("id")) # 212


# print(mydic["ids"]) # keyerror
# print(mydic.get("ids")) # nothing


# print(list(mydic.keys())) # ['id', 'name', 'roll']


# for key in mydic.keys():
#     print(key, end =" ") # id name roll 


# for value in mydic.values():
#     print(value, end =" ") # 212 Avishek 45 


# for key, value in mydic.items():
#     print(key, value)
# id 212
# name Avishek
# roll 45


# Methods....................
# update mehtods..................
ob1 ={
    2:2,
    3:3,
    4:4,
    5:5
}
ob2 ={
    6:6,
    7:7,
    8:8,
    9:9
}
# ob1.update(ob2)



# pop method.........................
# ob1.pop(6)
# print(ob1)

# popitem() - for delete last key value pair item ..........................
# del - delete whole dictionary
# del ob1
# del ob1[4]

# squarnum = {x: x**2 for x in range(10)}
# print(squarnum) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# keys = ["id", "name", "year"]
# default_value = 34
# newdict = dict.fromkeys(keys, default_value)
# print(newdict) # {'id': 34, 'name': 34, 'year': 34}


# Two list to a dictionary.......................
keys = ["id", "name", "year"]
default_value = [1, "Avishek", "4th"]
newdict = {}
# i = 0
# for key in keys:
#     newdict[key] = default_value[i]
#     i+=1
# print(newdict) # {'id': 1, 'name': 'Avishek', 'year': '4th'}


for i in range(0,3):
    newdict[keys[i]] = default_value[i]

# print(newdict) # {'id': 1, 'name': 'Avishek', 'year': '4th'}