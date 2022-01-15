
def verify_login(username, password):
    done = False
    loggedin = False
    database = open("database.txt", "r")
    username = username+"\n"
    password = password+"\n"
    while(done==False):
        line = database.readline()
        if(line == username):
            print("Now all we need is your password")
            userpassword = database.readline()
            if(userpassword == password):
                print("Welcome!")
                done = True
                loggedin = True
                return True
            else:
                print("Password is incorrect")
                done = True
                return False
        if(line == ""):
            done = True
            print("sorry you do not have an account with us")
    database.close()
