class Student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print("roll=",self.roll)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)
    def __str__(self):
        return self.name
f=open("student","r")
lst=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    lst.append(obj)
#print all student name having total>150

#for obj in lst:
    #if(obj.total>150):
     #   print(obj)
total=[]
for obj in lst:
    total.append(obj.total)
maximum=max(total)
for obj in lst:
    if obj.total==maximum:
        print(obj)

#conver names to uppercase
names=list(map(lambda obj:obj.name.upper(),lst))
print(names)
#print all student name having total>450
stud=list(filter(lambda obj:obj.total>450,lst))
for st in stud:
    print(st)














