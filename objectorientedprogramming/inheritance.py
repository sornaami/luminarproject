#inheritance

#single inheritance
class Parent:
    def phone(self):
        print("i have nokia phone")


class Child(Parent):
    pass


c=Child()
c.phone()