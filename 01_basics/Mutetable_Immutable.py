# String immutable
# name = "Avishek"
# username = name
# username = "Avi"
# print(username, name) # Avi Avishek

# Number immutable
# roll = 13
# newroll = roll
# newroll = 31
# print(roll, newroll) # 13 31

# List mutable
# l1 = [1,2,3,4]
# l2 = l1
# l2[0] = 44
# print(l1, l2) # [44, 2, 3, 4] [44, 2, 3, 4]

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# print(l1 == l2) # True
# print(l1 is l2) # False


# l1 = [1,2,3,4,5]
# l2 = l1
# print(l1 == l2) # True
# print(l1 is l2) # True
# l2 = [1,2,3,4,5]
# print(l1 == l2) # True
# print(l1 is l2) # False