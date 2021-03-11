#print all prime no between upper limit and lower limit
def prime(lower,upper):
    for i in range(lower,upper):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
lower = int(input("enter low limit"))
upper = int(input("enter upper limit"))
prime(lower,upper)


