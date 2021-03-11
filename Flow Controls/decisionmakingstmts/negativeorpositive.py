#read a number and chk for number is +ve or  -ve

num=int(input("enter your num"))
if(num>0):
   print("num is +ve")
elif(num<0):
    print("num is -ve")
elif(num==0):
    print("zero")
else:
   print("invalid no")