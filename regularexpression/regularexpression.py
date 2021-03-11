# regular exp used for pattern matching
#count no af ab in given string
string="ababababaaaabbbabb"

import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
for match in matcher:
    print(match.start()) #it will return positions of ab
    print(match.group())
    count+=1
print(count)
