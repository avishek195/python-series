weight = input("Enter your weight: ")
unit = input("(K)g or (L)ns: ")

if unit.upper == "K" :
    convert = float(weight) / 0.45
    print(f"Your weight in stones is: {convert}lbs")
else:
    convert = float(weight) * 0.45
    print(f"Your weight in stones is: {convert}kg")

