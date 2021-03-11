#calculate sum of odd and even numbers

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
sumeven=0
sumodd=0
for i in range(low,upp):
    if(i%2==0):
        sumeven=i+sumeven
    else:
        sumodd=i+sumodd
    i=i+1
    print("sum of even number is",sumeven)
    print("sum of odd number is",somodd)