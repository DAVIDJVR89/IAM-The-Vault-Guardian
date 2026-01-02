import hashlib
import string

symbols = string.punctuation

data_base = {}

def create_hash(password):
    resulting_hash = hashlib.sha256(password.encode()).hexdigest()
    return resulting_hash

def create_user():
    user = input("Insert your username: ")
    print("Username accepted.")
    print("--"*30)

    while True:
        password = input("Insert your password (should have at least one symbol, one number and one capital letter): ")
        print("--"*30)
        
        
        has_capital = False
        has_number = False
        has_symbol = False

        for caracter in password:
            if caracter.isupper():
                has_capital = True
            if caracter.isdigit():
                has_number = True
            if caracter in symbols:
                has_symbol = True
        
        if has_capital and has_number and has_symbol:
            data_base[user] = create_hash(password)
            print("Password accepted.")
            print("--"*30)
            print(f"User {user} and password successfully created.")
            print("--"*30)
            break
        else:
            print("ERROR: The password should have at least one capital letter, one number and one symbol.")
            print("--"*30)


    
def login():
    try_max = 3
    tries = 0

    print("---LOGIN---")
    while True:
       
        insert_user = input("User: ")
        if insert_user in data_base:
            print("Correct username. ")
            break
        else:
            print("Incorrect user, please try again.")
            continue
    
    while tries < try_max:
        current_attempt = tries + 1
        insert_password = input(f"Password ({current_attempt}/{try_max}): ")

        new_hash = create_hash(insert_password)
        if new_hash == data_base[insert_user]:
            print("Access authorized.")
            break

        else:
            tries += 1
            remaining = try_max - tries
            if remaining > 0:
                print(f"Wrong password. You have {remaining} tries left.")
                print("--"*30)
            else:
                print("--"*30)
                print("Maximum attempts exceeded. Your account has been blocked for security reasons.")
                print("--"*30)
                print("You can try again in 30 minutes.")
                print("--"*30)
                exit()
                
                
while True:
    print("---MENU---")
    print("1. Create user & password")
    print("2. Login")
    print("3. Check database")
    print("4. Exit")

    option = input("Please, select one of the options (1-4): ")
    print("--"*30)

    if option == "1":
        create_user()
    elif option =="2":
        login()
    elif option =="3":
        print(f"This is database: {data_base}")
    elif option =="4":
        print("See you next time !")
        exit()
    else:
        print("Wrong option, please try again.")
        break
