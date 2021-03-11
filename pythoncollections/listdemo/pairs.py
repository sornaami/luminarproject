lst=[1,2,3,4] #6 (2,4)
element=int(input("enter element"))
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp]
    if(total==element):
        print("pairs=",lst[low],",",lst[upp])
        break
    else:
        low+=1
#for item in lst:
    #for i in lst:
        #sum=(item!=i)
        #sum=item+i
        #print(sum)


#stack algorithm
#queue algorithm