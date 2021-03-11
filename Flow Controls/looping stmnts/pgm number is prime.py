#prime number checking
number=int(input("enter number"))
flg=0
for i in range(2,number):
    if(number%i==0):
        flg=1
        break
    else:
        flg=0
    if(flg>0):
        print("not prime")
    else:
        print("prime number")