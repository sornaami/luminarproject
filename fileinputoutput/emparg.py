#def printdetails()
f=open("employee","r")
employee={}
for lines in f:
    data=lines.rstrip("\n").split(",") # 1001,ajay,25000
    print(data)
    id=data[0]
    name=data[1]
    salary=data[2]
    exp=data[3]
    desig=data[4]
    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":salary,"exp":exp,"desig":desig}
    else:
        pass
for k,v in employee.items():
    print(k,",",v)

#def getDetails(eid):
#   if eid in employee:
#      print(employee[eid]["name"])
#  else:
#     print("employee doesnot exist with this eid")
#getDetails("1001")
#printdetails(id=10001) printemployee name who have id=10001
#printdetails(id=1001,property=salary)

def getemployeedetails(**args):
    print(args)
    eid=args["id"]
    prope=args["prop"]
    print(employee[eid]["name"])
    print(employee[eid][prope])

getemployeedetails(id="1001",prop="exp")

