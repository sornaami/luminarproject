text="hello hai hello hai how"
words=text.split(" ")
print(words)
dict={}
for word in words:     #chking for hello in dict
    if(word not in dict): #chking for hello is not in dict
        dict[word]=1
    else:
        dict[word]+=1
print(dict)

