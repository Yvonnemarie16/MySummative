#signup.py       
import object
        
def signupfunc ():
    print("thank you for considering this app")
    print("okay, What is you name")
    name = input()
    print("what is your age?")
    age = int(input())
    print("what is your email?")
    email = input()
    print("what is your password?")
    password = input()
    print("what is your location?")
    location = input()
    print("what is your current_weight?")
    current_weight = int(input())
    print("what is your target_weight?")
    target_weight = int(input())
    user = object.User(name,email,password,age,location,current_weight,target_weight)

    databasefile = open("database.txt","a")
    databasefile.write("New user\n")
    databasefile.write(name+"\n")
    databasefile.write(password+"\n")
    
    return user 