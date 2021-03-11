#print all even number in between lower limit and upper limit

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
if(lower>upper):
    print("upper should be greater than lower")
while(lower<=upper):
    if(lower%2==0):
        print(lower)
        lower+=1