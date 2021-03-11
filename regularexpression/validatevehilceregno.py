#kl 2digits 2alpha
import re
vehicleno=input("enter vehicle no")
rule="kl[0-9]{2}[a-z]{2}\d{4}"
match=re.fullmatch(rule,vehicleno)
if(match==None):
    print("Invalid")
else:
    print("valid")

#task #validate all gmail ids in text file
#write file in another

