from re import *

pattern="aaaaabbaabbbaaaabaaa"
#x="a+" #will check for single a and sequences of a
#x="a*"
#x="a?" #checking all positions including not a
#x="^a" is the given pattern starting with a
#x="a$" is the given pattern end with a
#x="a{2}" will check for 2 numbers of a
x="a{2,3}"#minimum 2 a and maximum 3 a
matcher=finditer(x,pattern)
for match in matcher:
    print(match.start())
    print(match.group())