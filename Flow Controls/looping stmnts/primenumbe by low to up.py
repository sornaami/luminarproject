
#low=10
#upp=50
#print all prime number by low to upp

low=int(input("enter low limit")) #10
upp=int(input("enter upper limit")) #50
for number in range(low,upp):
    if(number>1):
        for i in range(2,number):
            if(number%i==0):
                break
        else:
            print(number)

