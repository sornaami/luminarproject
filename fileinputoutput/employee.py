f=open("employee","r")
ename=[]
esal=[]
for lines in f: # 1001,ajay,25000\n
    line=lines.rstrip("\n") # 1001,ajay,25000
    data=line.split(",")  #data=[1001,ajay,25000]
    name=data[1]
    salary=data[2]
    ename.append(name)
    esal.append(salary)
print(ename)
print(esal)



