#variables name rules it should be alphabet a-z
#any number of charcters
#first char should be an alphabet within ato k
#second char should be number it is divisble by 3
#folloeing by any words
import re
rule="[a-k][369][a-z0-9]*"
pattern=input("enter variable name")
matcher=re.fullmatch(rule,pattern)
if(match==None):
    print("invalid")
else:
    print("valid variable number")