class Employee:
    company_name="luminar"
    def __init__(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printEmp(self):
        print("eid=",self.id)
        print("designation=",self.desig)
        print("salary=",self.salary)
        print("companyname=",Employee.company_name)
emp=Employee(1001,"devops",40000)
emp.printEmp()



#constructor used for initializing variable
#constructor name is always __init__
#constructor is automaticalyy invoked at the time of object creation