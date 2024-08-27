strs = "aabbcddd"
# print(strs.count("a"))
for i in strs:
    if strs.count(i) == 1:
        print(f"Non repeacted character is {i}")