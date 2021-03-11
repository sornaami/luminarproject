class Parent:
    def property(self):
        print("will give 10 kg gold anf 2 lakh cash")
    def marriage(self):
        print("marriage fixed with sam")
class Child(Parent):
    def marriage(self):
        print("marriage with siva")
c=Child()
c.marriage()
c.property()

