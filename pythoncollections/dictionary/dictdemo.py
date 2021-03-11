#how to define dictionary

#dict={}

#values stored in dictionary in form of key:value pairs
#id:101
#name="ajay"
#salary:25000

employee={"id":101,"name":"ajay","salary":25000}

#we can store both same and didderent type of data
#duplicate key is not allowed
#duplicate value allowed

print(employee)
#if we want to access any value we have to use corresponding key
print(employee["name"])
print(employee["salary"])

#add key,  gender:male
employee["gender"]="male"
print(employee)

#update
#update salary as 30000
employee["salary"]=+5000
print(employee)

#checking for a specific key
print("designation in employee")