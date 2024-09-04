

# def missingCharacters(s):
#     # Write your code here
#     digits = ["0","1","2","3","4","5","6","7","8","9"]
#     leter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     for i in s:
#         print(i)
#         if i in digits:
#             digits.remove(i)
#         if i in leter:
#             leter.remove(i)
#     result = ""
#     for digit in digits:
#         result = result + digit
#     for leters in leter:
#         result = result + leters
        
#     return result

# print(missingCharacters("8hypotheticall024y6wxz"))

# list = [[1, 2, 7], [4, 5, 6], [8, 8, 9]]


# for i in range(0, len(list)):
#     for j in range(0, len(list[i])):


# def printfunction(num):
#     numbers = "0123456789"
#     result = ""
#     while num > 0:
#         result = numbers[num % 10]  + result
#         num = num // 10
#     return result


# n = 12
# result = ""
# for i in range(1,n+1):
#     result = result + printfunction(i)
    
    
# print(result)
# print(150 % 10)
# print(10 % (n +1))


# num = "100,000,000.000"

# l = num.split(",")
# print(l)

# st = "AABCAAADA"
# start = 0
# end = 3
# newset = set()
# for i in range(0, len(st)):
#     if i == start:
#         print(st[start:end])
#         newset.add(st[start:end])
#         start += 3
#         end +=3
    
# print(newset)


# def delete_dup(st):
#     result = ""
#     for char in st:
#         if char not in result:
#             result += char
#     print(result)

# def merge_the_tools(string, k):
#     # your code goes here
#     n = len(string)
#     num = n//k
#     start = 0
#     end = num
#     for i in range(0, n,k):
#             leter = string[i:i+k]
#             delete_dup(leter)

# merge_the_tools("AABCAAADA", 3)

# st = "avishek"
# result = ""
# for i in range(0,len(st)):
#     if i == 2:
#         result += "y"
#     else:
#         result += st[i]
# print(result)

s = "qA3"

# print(any(c.isalnum() for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))

# inputs = "235678"
# print(list(map(int,inputs.split())))
digits = "234"
dic = {
        "2":"a b c",
        "3":"d e f",
        "4":"g h i",
        "5":"j k l",
        "6":"m n o",
        "7":"p q r s",
        "8":"t u v",
        "9":"w x y z"
    }

# result = []
# num = [dic[digit].split() for digit in digits]
# print(num)

# def fun(num):
#     return num + 100 if num > 10 else num
# newnum = list(map(fun, [1,4,40,20]))
# print(newnum)


def fun(num):
    return num > 10
newnum = list(map(lambda x : x + 10 if x > 10 else x, [1,4,40,20]))
print(newnum)