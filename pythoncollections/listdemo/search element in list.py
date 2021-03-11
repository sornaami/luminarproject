lst=[10,11,12,13,14,15,16,17]
elem=int(input("enter element"))
flag=0
for item in lst: #10, 11
    if(elem==item):#11==10 not increased, 11==11
        flag+=1
        break
    if(flag==0):
        print("not found")
    else:
        print("element found")