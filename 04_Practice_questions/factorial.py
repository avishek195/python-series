num = 4

factorial = 1

# for i in range(1,num+1):
#     factorial *= i
# print(f"The factorial of {num} is {factorial}")
i = num
while i > 0:
    factorial *= i
    i -=1
print(f"The factorial of {num} is {factorial}")