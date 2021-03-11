#print second largest no

number1=int(input("enter value for number 1:"))
number2=int(input("enter value for number 2:"))
number3=int(input("enter value for number3:"))
if((number1>number2)&(number1<number3)):
    print("second largest number is : number1")
elif((number2>number1)&(number2<number3)):
    print("second largest number is : number2")
elif((number3>number2)&(number3<number1)):
    print("second largest no is : number3")
