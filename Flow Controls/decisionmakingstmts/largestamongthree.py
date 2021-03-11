#read three numbers and print largest among three

number1=int(input("enter value for number1"))
number2=int(input("enter value for number2"))
number3=int(input("enter value for number3"))

if((number1>number2)&(number1>number3)):
    print("number1 is the largest number")
elif((number2>number1)&(number2>number3)):
    print("number2 is the largest number")
elif((number3>number1)&(number3>number2)):
    print("number3 is the largest number")
elif((number1==number2)&(number1==number3)):
    print("all numbers are equal")

    #print second largest no