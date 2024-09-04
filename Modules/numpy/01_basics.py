import numpy as np

# Using Array..... 
# arr = np.array([1,3,4,5,6,7])
# print(arr)

# for i in arr:
#     print(type(i))

# Using Tuple.....
# arr = np.array((1,3,4,5,6,7))
# print(arr)

# for i in arr:
#     print(type(i))


#Indexing......

# arr = np.array([[1,3,4,5,6],[2,4,6,8,9]])

# print(arr[0,0])
# print(arr[0][0])


# Python dataTypes.....

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Numpy DataTypes.....

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta 
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )



arr = np.array([1.1,3.2,4.4,5.6,6.9,7.4])
print(arr)
newarr = arr.astype("i")
print(newarr)

