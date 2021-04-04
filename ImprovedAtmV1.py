import random
from datetime import datetime

database = {}

def init():

    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have an account with us? Press 1 (for yes) 2 (for no)\n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected an invalid option")
        init()

def login(count = 0):
    if(count < 3):

        print("***** Login *****")

        accountNumberFromUser = int(input("What is your account number?\n"))
        password = input("What is your password?\n")

        for accountNumber, userDetails in database.items():
            if(accountNumberFromUser == accountNumber):
                if(userDetails[3] == password):
                    currentDateTime = datetime.now()
                    dateReadable = currentDateTime.strftime("%d/%m/%Y %H:%M:%S")
                    print("Current login time is %s" % dateReadable)
                    bankOperation((userDetails))

        print('Invalid account or password')
        count +=1
        login(count)

    else:
        print("Account locked.")
        exit()


def bankOperation(user):
    print("\nWelcome %s %s" % (user[0], user[1]))

    selectedOption = int(input("What would you like to do?  Press 1 to deposit.  Press 2 to withdraw.  Press 3 to logout.  Press 4 to exit.\n"))

    if (selectedOption == 1):
        depositOperation(user)
    elif (selectedOption == 2):
        withdrawlOperation(user)
    elif (selectedOption == 3):
        login()
    elif (selectedOption == 4):
        exit()
    else:
        print("Invalid Option")

def withdrawlOperation(user):
    if(user[4] > 0):
        print("You're current balance is %d" % user[4])
        withdrawlAmount = int(input("How much would you like to withdrawl?\n"))
        if(withdrawlAmount > user[4]):
            print("Cannot withdraw more than %d, returning to the main menu" % user[4])
            bankOperation(user)
        else:
            user[4] -= withdrawlAmount
            print("Withdrew %d, remaining balance is %d" % (withdrawlAmount, user[4]))
            print("Returning ot the main menu")
            bankOperation(user)
    else:
        print("You're current balance is $0.00, you must deposit more money before you can withdrawl.")
        bankOperation(user)

def depositOperation(user):
    depositAmount = int(input("How much would you like to deposit today?\n"))
    if(depositAmount > 0):
        user[4]+=depositAmount
        print("Hi %s, your balance is %d.  Taking you back to the main menu." % (user[0], user[4]))
        bankOperation(user)
    else:
        print("You must deposit an amount greater than zero, bringing you back to the main menu.")
        bankOperation(user)

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def register():
    print("***** Register *****")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("Enter your email address?\n")
    currentBalance = 0
    password = "a"
    reEnterPassword = "b"
    while(password != reEnterPassword):
        password = input("Enter a password?\n")
        reEnterPassword = input("Re enter your password\n")
        if(password != reEnterPassword):
            print("Try again, passwords do not match.")

    accountNumber = generateAccountNumber()

    print("Your account has been created")
    print("_____________________________")
    print("Your account number is: %d" % accountNumber)
    print("_____________________________")

    database[accountNumber] = [first_name, last_name, email, password, currentBalance]
    login()

def logout():
    login()

init()