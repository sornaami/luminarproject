# *numbers means can add many numbers

def add(*numbers):
    print(sum(numbers))

add(10,20,30,40,50,60)

def person(**args):
    print(args)
person(name="ajay",joblocation="kakkanad",homelocation="trivandrum",salary="30000")
