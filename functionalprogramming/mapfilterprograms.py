#map,filter,reduce
#square=number *functionfor square=o/p(map)
#def squares(num):
   # return num*num

numbers=[1,2,3,4,5,6]
data=list(map(lambda num:num*num,numbers)) #2 args function,iterable
print(data)
#filter even numbers from list

def even(num):
    return num%2==0
even=list(filter(even,numbers))
print(even)

