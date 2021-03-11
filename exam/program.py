#HHHPPSDAAA
#3H2P1S1D3A
text="HHHPPSDAA"
dict={}
for char in text:
    if(char not in dict):
        dict[char]=1
    else:
        dict[char]+=1

print(dict)
op=""
for k,v in dict.items():
    op=op+str(v)+k
    print(op)