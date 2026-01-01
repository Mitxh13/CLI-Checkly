import authentication
print("Welcome to Checkly!!")
print("********************\n")

def landing():
    print("Please Login to continue to main dashboard!")
    print("1.Login to checkly \n 2.Create an New account")
    choice_login = int(input("Enter your Preference: "))
    match(choice_login):
        case(1):
            print("---redirecting to login page---")
            authentication.login()
        case(2):
            print("---redirecting to Account Creation page---")
            authentication.NewUser()
        case(3):
            print("Closing the program safely!!")
