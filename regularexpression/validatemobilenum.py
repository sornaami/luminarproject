import re
mobile=input("enter mobile num")
rule="(91)?\d{10}"
match=re.fullmatch(rule,mobile)
if(match==None):
    print("invalid")
else:
    print("valid mobile number")

