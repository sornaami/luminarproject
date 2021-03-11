from functools import *


class employee:
    cname = "luminar"

    def __init__(self, empid, name, sal, desig):
        self.id = empid
        self.name = name
        self.sal = sal
        self.desig = desig

    def printVal(self):
        print(" id :", self.id)
        print(" name :", self.name)
        print(" salary :", self.sal)
        print(" desig :", self.desig)

    def __str__(self):
        return self.name


f = open("employee", "r")
lst = []
for data in f:
    data = data.rstrip("\n").split(",")
    id = data[0]
    name = data[1]
    sal = int(data[2])
    desig = data[3]

    obj = employee(id, name, sal, desig)
    lst.append(obj)
name = list(map(lambda obj: obj.name.upper(), lst))
print(name)

maxsal = reduce(lambda num1, num2: num1 if num1 > num2 else num2, list(map(lambda obj:obj.sal,lst)))
print(maxsal)
totsal = reduce(lambda num1, num2: num1 + num2, list(map(lambda obj : obj.sal,lst)))
print(totsal)
ans = list(filter(lambda obj: obj.desig == "trainer", lst))                             # getting empty list, WHY?????
for d in ans:
    print(d,"developer")                                                                               # no output








# without list
#     totsal = reduce(lambda num1, num2: num1 + num2,list(map(lambda obj : obj.sal,lst)
#     maxsal = reduce(lambda num1, num2: num1 if num1 > num2 else num2,list(map(lambda obj : obj.sal,lst )
    # ans = list(filter(lambda obj: obj.desig == "trainer", list(map(lambda obj: obj.desig, lst))))

