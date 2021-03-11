#123=1*1*1+2*2*2+3*3*3=36

number=int(input("enter number"))
res=0
while(number!=0):#5
    digit=number%10 #5%10
    res=(res)+(digit**3)
    number=number//10
    print(res)
