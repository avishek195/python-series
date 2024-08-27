import json

def get_All_Users():
    try:
        with open("bank_user.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def set_user(users):
    with open("bank_user.txt","w") as file:
        json.dump(users, file)

def login(users):
    print("\n")
    name = input("Enter your name: ")
    password = input("Enter your passwword: ")
    for user in users:
        if user["name"] == name and user["password"] == password:
            print("You are successfully login")
            return user
    print("Invalid name or password")
    return
 
def withdraw_money(users):
    user = login(users)
    amount = int(input("Enter your withdrawal amount: "))
    if user["Balance"] - amount < 0:
        print("Insufficient balance")
        return
    user["Balance"] -= amount
    print(f" Rs.{amount} Amount successfully withdrwal")
    set_user(users)

def check_balance(users):
    user = login(users)
    print(f" You Have {user['Balance']} in your account")

def deposit_money(users):
    user = login(users)
    amount = int(input("Enter your amount: "))
    user["Balance"] += amount
    print(f" Rs.{amount} Amount successfully credit")
    set_user(users)
    
    


def create_account(users):
    print("Enter your details: ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirmpass = input("Enter password again: ")
    if password != confirmpass:
        print("Password does not match")
        return
    current_balance = 0
    users.append({"name": name, "email": email, "password": password, "Balance": current_balance})
    set_user(users)

def main():
    users = get_All_Users()
    # This is the  main function of Bank Managment
    print("*" * 70)
    print()
    print("                         Welcome to ATM")
    print()
    print("*" * 70)

    while(True):
        print("0. create account")
        print("1. Withdrwal Money")
        print("2. Check Balance")
        print("3. Diposite Money")
        print("4. Exit")

        choice = input("Enter your option: ")

        match choice:
            case "0":
                create_account(users)
            case "1":
                withdraw_money(users)
            case "2":
                check_balance(users)
            case "3":
                deposit_money(users)
            case "4":
                print("Thank you for using our ATM")
                exit()
            case _:
                print("Invalid option. Please choose a valid option.")

    

if __name__ == "__main__":
    main()