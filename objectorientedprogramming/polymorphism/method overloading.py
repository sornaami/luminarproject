class Maths:
    def add(self):
        num1,num2=10,20
        print(num1+num2)
    def add(self,num1):
        num2=50
        print(num1+num2)
    def add(self,num1,num2):
        print(num1+num2)

ob=Maths()
ob.add(10,20)
ob.add(10)

#same method name and different number of arguments


#recently called will execute