#print numbers between low limit and upper limit

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
if(lower>upper):
    print("upper should be greater than lower")
while(lower<=upper):
    print(lower)
    lower+=1