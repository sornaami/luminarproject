class Employee:
    def __init__(self,id,name,salary,desig):
        self.id=id
        self.name=name
        self.salary=salary
        self.desig=desig
    def printEmployee(self):
        print("id=", self.id)
        print("name=", self.name)
        print("salary=", self.salary)
        print("desig=", self.desig)
    def __str__(self):
        return self.name
f=open("employee","r")
lst=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    id=data[0]
    name=data[1]
    salary=int(data[2])
    desig=data[3]
    obj=Employee(id,name,salary,desig)
    lst.append(obj)
    print(obj)

#convert all emplo to uppercase

    names = list(map(lambda obj: obj.name.upper(), lst))
    print(names)

#find all emplo desig developer

develop=list(filter(lambda obj:obj.desig=="developer",lst))
for d in develop:
    print(d,"developer")
#find total salary of all emplo
from functools import *
total=reduce(lambda salary1,salary2: salary1 + salary2,list(map(lambda obj : obj.salary,lst)))
print(total)



#find high salar employee
max=reduce(lambda salary1,salary2:salary1 if salary1>salary2 else salary2,list(map(lambda obj:obj.salary,lst)))
print(max)
















