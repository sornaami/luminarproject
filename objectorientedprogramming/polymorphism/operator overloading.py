class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages

    def __sub__(self,other):
        return self.pages-other.pages

    def __mul__(self,other):
        return self.pages*other.pages

    def __truediv__(self, other):
        return self.pages/other.pages

    def __str__(self):
        return str(self.pages)

obj=Book(150)
print(obj)

obj1=Book(200)
print(obj1)
print(obj+obj1)
print(obj-obj1)
print(obj*obj1)
print(obj/obj1)

# +operator is used for integer addition and string concatination
