employees=[[100,"ajay",25000],[101,"vijay",22000],[102,"bincy",27000],[103,"jino",30000]]

#pgm to print all employee names only
for data in employees:
    print(data[1])



#calculate sum of salary
total=0
for data in employees:
    total=total+data[2]
print(total)

#print all employee salary greater than 25000

for data in employees:
    if(data[2]>25000):
        print(data[1])






