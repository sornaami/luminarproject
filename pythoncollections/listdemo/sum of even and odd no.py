lst=[11,12,13,14,15,16,17]
oddsum=0
evensum=0
for item in lst:
    if(item%2==0):
        evensum=evensum+item
    else:
        oddsum+=item
print(oddsum)
print(evensum)
