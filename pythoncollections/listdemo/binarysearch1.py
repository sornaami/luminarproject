#input list or array
#step sor
ar=[6,4,5,2,1,3]
#step sorting
ar.sort()
print(ar)
low=0
upp=len(ar)
flag=0
element=int(input("enter element for searching"))
while(low<=upp): #0<6 4<6
    mid=(low+upp)//2 # mid=3 4+6//2=5
   #[1,2,3,4,5,6]
#case1
    if(element>ar[mid]): #5>ar[3] 5>4 5>5
        low=mid+1         #low=3+1=4
    elif(element<ar[mid]):  #5<5
        upp=mid-1
    elif(element==ar[mid]): #5==5
       flag=1
       break
    if(flag>0):
        print("not found")
    else:
        print("element found")