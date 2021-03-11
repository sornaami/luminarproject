import re
#f=open("gmail","r")
#email={}
#for lines in f:
#    data=lines.rstrip("\n")
email=input("enter email")

rule="[a-z0-9\W]*@gmail.com"
match=re.fullmatch(rule,email)
if(match==None):
    print("invalid")
else:
    print(email)