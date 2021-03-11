import re

#predefines character sets
#x="[abc]" # it will check either a,b, or c is present in target string
#x="[a-z]" #it will check a to z lower alphabets
#x="[0-9]" will check for digits
#x="[A-Z]"
#x="[a-zA-Z]"
#x="[a-zA-Z0-9]" #will check for all words
#x="[^a-zA-Z0-9]" # except ato z
#x="[^0-9]"
#predefined charcters
#x="\s" #it will check for space location
#x="\d" will check for digit==[0-9]
#x="\D" except digit prints all
#x="\w"[a-zA-Z0-9] any words
x="\W" #special characters[^a-zA-Z0-9][space and @]
matcher=re.finditer(x,"ab7 c@KZ")
for match in matcher:
    print(match.start())
    print(match.group())
