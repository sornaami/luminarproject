import datetime
class Person:
    def setPerson(self,name,age):
        self.name=name
        self.age=age
    def printPerson(self):
        print(self.name,",",self.age)
class Bank(Person):
    bank_name="Sbk"
    def createAccount(self,acno):
        self.acno=acno
        self.balance=3000
    def deposit(self,amount):
        self.balance+=amount
        print("your",Bank.bank_name,"has been credited with",amount,"aval balance",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance in your account")
        else:
            self.balance-=amount
            print("your",Bank.bank_name,"has been debited with",amount,"on",datetime.date.today(),"aval balance",self.balance)
obj=Bank()
obj.setPerson("samvi",27)
obj.printPerson()
obj.createAccount(1001)
obj.deposit(5000)
obj.withdraw(1000)

#difrnt types of variables
#1 instance variables = always related to object
#2 static variables= can be accessed using class name
#static can be used for efficient memory usage
#static related to class