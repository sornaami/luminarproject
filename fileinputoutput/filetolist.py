f=open("numbers","r")
lst=[]
for numbers in f:
    #remove /n
    number=int(numbers.rstrip("\n"))
    lst.append(number)
print(lst)

#find sum of list
total=sum(lst)
print("sum=",total)

#find maximum no from list
large=max(lst)
print("largest=",large)

#print minimum no from lst
low=min(lst)
print("minimum number=",low)

