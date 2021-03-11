#class--- plan,design,blueprint
#object--real world entity
#reference--perform opn over object

#syntax
#class Classname:
#methods

class Person:

    def setValues(self,ag,nam):
        self.age=ag
        self.name=nam

    def printValues(self):
        print("age=",self.age)
        print("name=",self.name)

#object syntax referencename=ClassName()
obj=Person()
obj1=Person()
obj1.setValues(26,"vijay")
obj.setValues(27,"aijay")