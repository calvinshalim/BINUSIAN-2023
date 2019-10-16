#%% "_" = public but dont change outside the class
# "__" = private, can only change in the class
#cara pakai class tuh pakai "." Ex = myAccount."def function yg dibuat"()
import json
# ACCOUNT (1)
class Account:
    __balance = 0
    
    def __init__(self,balance2): #<< is a must cos its a property called "initializer"
        self.__balance = balance2
        
    def getBalance(self):
        return self.__balance
        
    def deposit(self,amt):
        if amt > 0:
            self.__balance = self.__balance + amt
            return True
        else:
            return False

    def withdraw(self,amt):
        try:
            if amt <= 0:
                return False
            else:
                self.__balance -= amt
                return True
        except TypeError:
            return False
        
myAccount = Account(5000)
myAccount.__balance = 1000000

#CUSTOMER (2)
class Customer:
    __fname=""
    __lname =""
    __password =""
    __account= Account(5000)
    
    def __init__(self,fname,lname,password):
        self.__fname =fname
        self.__lname = lname
        self.__password = password
    
    def getpassword(self):
        return self.__password
    
    def getfname(self):
        return self.__fname
        
    def getlname(self):
        return self.__lname
    
    def getAccount(self):
        return self.__account
    
    def setAccount(self,acct):
        self.__account = acct
        
#Ex. create a customer 
#fc = Customer("calvin","halim")
#fc.setAccount(Account(9000))
#print("Customer balance is >>",fc.getAccount().getBalance())

#BANK (3)
class Bank:   
    customer={}
    num_of_cust = 0
    bankName=""   
    def __init__(self,bname):
        self.bankName = bname

    def addcustomer(self,username,fname,lname,password):
        self.num_of_cust += 1
        self.customer[username] = Customer(fname,lname,password)
        
    def get_numcustomer(self):
        return (self.num_of_cust)
    
    def getcustomer(self,index):
        return self.customer[index]
    
bank = None
def loadjson():
    global bank
    with open("databaseBank.json")as f:
        x = json.load(f)
    bank = Bank(x["BankName"])
    for c,v in x["Customer"].items():
        bank.addcustomer(c,v["fname"],v["lname"],v["password"])

def login():
    global bank
    username = input("Enter username :")
    password = input("Enter password :")
    if username == "admin" and password == "admin":
        menuAdmin()
    elif username in bank.customer:
        if password == bank.customer[username].getpassword():
            menucustomer(username)
        

def menucustomer(username):
    print("    WELCOME TO CLVN BANK")
    print("="*10,"OPTIONS","="*10,"\n1.DEPOSIT\n2.WITHDRAW\n3.EXIT\n","="*28)
    while True:
        print("Balance :",bank.customer[username].getAccount().getBalance())
        choice = input(">>>")
        if choice == "1":
            amt = int(input("Enter Amount "))
            if bank.customer[username].getAccount().deposit(amt):
                print("Deposit Successful!")
            else:
                print("Deposit Unsuccessful!")
        elif choice == "2":
            amt = int(input("Enter Amount :"))
            if bank.customer[username].getAccount().withdraw(amt):
                print("Withdraw Successful!")
            else:
                print("Insufficient Amount!")
        elif choice == "3":
            break
        
        else:
            pass

def menuAdmin():
    print("       ADMIN CLVN BANK")
    print("="*10,"OPTIONS","="*10,"\n1.ADDCUST\n2.EXIT\n","="*28)
    while True:
        choice = input(">>>")
        if choice =="1":
            fname = input("First Name :")
            lname = input("Last Name :")
            username = input("New Username :")
            password = input("New Password :")
            bank.addcustomer(username,fname,lname,password)
        elif choice == "2" :
            break
        else :
            pass

def savejson():
    x = {}
    x["BankName"] = bank.bankName
    x["Customer"] = {}
    for a,b in bank.customer.items():
        x["Customer"][a]={
            "fname": b.getfname(),
            "lname": b.getlname(),
            "password": b.getpassword(),
            "account": {
                    "balance": b.getAccount().getBalance()
                }
            }
    with open("databaseBank.json","w+") as f:
        json.dump(x,f)
        
loadjson()
login()
savejson()