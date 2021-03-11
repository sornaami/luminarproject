lst=[1,2,5,6,7]
data=[x-1 if x<5 else x+1 if x>5 else x for x in lst]
print(data)


#((1,4),(1,5),(1,6),(2,4))
lst=[1,2,3]
lst1=[4,5,6]
pairs=[]
for i in lst:
    for j in lst1:
        pairs.append(lst)
        print((i,j))
#list comprehension
output=[(i,j)for i in lst for j in lst1]

lst=[1,2,3,4,5,6]
squares=[i*i for i in lst]
print(squares)


#output=list(map(lambda num1:num**2,lst))
#print(output)

#output=[num**2 for num in lst]
#print(output)

even=[num for num in lst if num%2==0]
print(even)

output=[i+1 if i>5 else i-1 for i in lst]
print(output)

