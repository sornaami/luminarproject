f=open("complete.csv","r")
fout=open("covidoutput.txt","w")
dict={}
for lines in f:
   data=lines.rstrip("\n").split(",")
   state=data[1]
   cases=float(data[4])
   if(state not in dict):
      dict[state]=cases
   else:
      dict[state]=cases
   print(dict)
lst=[]
for k,v in dict.items():
   lst.append((v,k))
   lst=sorted(lst,reverse=True)
   print(lst[0])

for val in lst:
   fout.write(string(val)+"\n")