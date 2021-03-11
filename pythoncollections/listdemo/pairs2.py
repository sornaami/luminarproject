lst=[1,2,3,4] #6 (2,4)
element=int(input("enter element"))
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp] #1+4=5 2+4
    if(total==element): #5==6 5==7
        print("pairs",lst[low],",",lst[upp])
        break
    elif(total>element): #5>6
        upp=upp-1
    elif(total<element): #5<6
        low+=1




