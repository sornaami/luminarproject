#create a student dictionary with total
student={"role no":5,"name":"samvi","total":50}
print(student)

print(student["name"])

print("college" in student)
student["college"] ="luminar technolab"
print(student)

student["total"]=100
print(student)

#for key in student:
    #print(key) -->only key value roleno, name, total will be printed
for key in student:
    print(key,"",student[key])
