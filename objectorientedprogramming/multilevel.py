class Parent:
    def m1(self):
        print("inside parent1")
class Child(Parent):
    def m2(self):
        print("inside Child")

class SubChild(Child):
    def m3(self):
        print("inside subChild")

sb=SubChild()
sb.m3()
sb.m2()
sb.m1()

sb2=child()
sb2.m2()
sb2.m1()
#sb2.m3() =error didnt inherit child