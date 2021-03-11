f=open("temp","r")
fout=open("tempoutput","w")
dict={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    print(data)
    dist=data[0]
    temp=data[1]
    if (dist not in dict):
        dict[dist]=temp
    else:
        maxm=max(temp,dict[dist])
        dict[dist]=maxm
print(dict)

lst=[]
for k,v in dict.items():
    lst.append((k,v))
for val in lst:
   fout.write(str(val))



