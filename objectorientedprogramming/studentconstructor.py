class Student:
    college="BITS"
    def __init__(self,roll_no,name,course,total):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print("roll_no=",self.roll_no)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)
        print("college",Student.college)
    def __str__(self):
        return self.name



obj=Student(5,"samvi","B.tech",1000)
obj1=Student(6,"moukthi","IT",900)

print(obj) #here printing object__Str__(self) to string()
print(obj1)
#obj class is the parent class for all classes by default