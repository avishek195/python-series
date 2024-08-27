user = "Avishek"
newuser = ""
# for i in range(0,len(user)):
#     newuser += user[len(user)-i- 1]


for char in user:
    newuser = char + newuser


print(newuser)