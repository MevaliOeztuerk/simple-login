#########################################################
# creator: Mevali Öztürk
# latest update: 10.09.2021
#########################################################

import re

#Todo: use a hash lib like "passlib"
#Todo: Build GUI
#Todo: check if the password is safe enough
#Todo: use DB instead of txt-file

class login():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.name_regex = re.compile(r'''
            #name:pw
            [a-zA-Z0-9_.+]+        # username part    []+ means: search vor one ore more 
            :                      # : symbol
            ''',re.VERBOSE)
        self.pw_regex = re.compile(r'''
            #name:pw
            :                      # : symbol
            [a-zA-Z0-9_.+]+        # password part
            ''',re.VERBOSE)

    def writeDatabase(self):
        with open("Database.txt", "a") as db:
            data = "{}:{}".format(self.username, self.password) + "\n"
            db.write(data)

    def readDatabase(self):
        with open("Database.txt", "r") as db:
            database = db.readlines()
            for account in database:
                account_name = self.name_regex.findall(account)[0].replace(":", "")
                account_pw = self.pw_regex.findall(account)[0].replace(":", "")
                if account_name == self.username:
                    return True, account_name, account_pw
            return False, account_name, account_pw

    def signIn(self):
        print("Login")
        while (True):

            self.username = input("Name: ").strip()
            self.password = input("Password: ").strip()

            account_bool, account_name, account_pw = self.readDatabase()

            if account_bool is True:
                if account_pw == self.password:
                    print("Signed In!")
                    break
                else:
                    print("wrong password")
            else:
                print("Account name doesnt exist!")

    def signUp(self):
        print("SignUp")
        while (True):
            self.username = input("Name: ").strip()
            self.password = input("Password: ").strip()

            account_bool, account_name, account_pw = self.readDatabase()

            if account_bool is False:
                self.writeDatabase()
                btn = input("go back to Login? (y/n)")
                if btn == "y" or btn == "Y":
                    self.signIn()
                else:
                    break
            else:
                print("Name already exists, try again")

if __name__ == '__main__':
    logIn = login()
    btn = input("Do you want to Login(y) or SignUp(n)?")
    if btn == "y" or btn == "Y":
        logIn.signIn()
    else:
        logIn.signUp()
