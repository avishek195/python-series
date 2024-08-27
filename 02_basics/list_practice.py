# list1 = [2,3,2,6,3,3]
# # newset = set( x for x in list1)
# newset = set()
# newset.update(list1)
# print(newset)
# for i in list1:
#     print(list1.count(i))
#     if list1.count(i) >= 2:
#         list1.remove(i)

# list1 = [x for x in newset]
# print(list1)


# nums = [1,1,2]
# # print(len(nums))
# nums.clear()
# nums = [1]
# print(nums)

# for i in range(1,len(nums)):
#     print(i-1, i)

# for i in range(1,len(nums)):
#     # print(i)
#     print(nums[i], nums[i-1])
#     if nums[i-1] == nums[i]:
#         nums.remove(nums[i])

# print(nums)




# Set
# List
# Tupel
# Dictionary


# Set
set = {"name", "sec", "year", "sec"}
# print(set) # {'year', 'sec', 'name'}

# set.add(24)
# print(set) # {24, 'name', 'sec', 'year'}


# set.update([4,5,7,9])
# print(set) # {4, 5, 7, 'sec', 9, 'name', 'year'}


# set.update({4,5,7,9})
# print(set) # {4, 5, 7, 'sec', 9, 'name', 'year'}


# set.update({4,5,7,9})
# print(set) # {4, 5, 7, 'sec', 9, 'name', 'year'}

# set.discard("secd")
# print(set)

# set.pop()
# set.difference_update({"name"})
# print(set)


# import json
# #list

# list = []

# list.append({"name": "avishek", "Roll": 13})
# list.append({"name": "soumitra", "Roll": 26})
# list.append({"name": "soumitra", "Roll": 26})

# # for item in enumerate(list):
# #     print(item)

# def save_file():
#     with open("newtext.txt", "w") as file:
#         json.dump(list,file)

# def print_data():
#     with open("newtext.txt", "r") as file:
#         return json.load(file)
# save_file()
# for item in enumerate(print_data()):
#     print( item)

# print(list)


# dictionary

# dics ={
#     "name": "avishek",
#     "Roll": 13,
#     "age": 22

# }

# # print(dics.get("name"))
# dics.update({"year": "4th"})
# dics.update({"name": "Avishek"})

# # dics.pop("name")
# dics.setdefault("years", "5th")

# print(dics)

# Tupel

