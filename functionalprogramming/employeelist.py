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

#find all emplo desig developer
result=[obj.name for obj in lst if obj.desig=="developer"]
print(result)

nam=[obj.name.upper() for obj in lst]
print(nam)

ot=sum([obj.salary for obj in lst])
print(ot)

high=max([obj.salary for obj in lst])
print(high)







