# num = input("Enter any number: ")
# try:
#     for i in range(1,11):
#         print(f"{num} X {i} = {int(num) * i}")
# except Exception as e:
#     print(f"{e}")

num = int(input("Enter any number: "))

if num>5:
    raise Exception("Enter value between 5 and 9")