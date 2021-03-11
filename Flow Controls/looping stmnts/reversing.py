#program to revers 123 to 321
number=int(input("enter value for number"))
res=0
while(number!=0):
    digit=number%10
    res=(res*10)+digit
    number=number//10
    print(res)