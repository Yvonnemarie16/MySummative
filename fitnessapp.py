#dashboard.py
import verify
import signup
import object

print("Hello user, would you like to signin or signup")
response = input()

if (response == "signin"):
    print("great, whats your name?")
    user = input()
    print("wonderful, whats your password ?")
    password = input()
    loggedin = verify.verify_login(user,password)
    if (loggedin == True): 
        print("welcome back")   


if (response == "signup"):
    done = False 

    while(not done):
        print("so you would like to create an account with us?")
        response = input()
        if (response == "yes"):
            signup.signupfunc()
            print("congratulation, you've made an account!!")
            done = True
        elif(response == "no"):
            print("ok bye")
            done = True
        
        
        

