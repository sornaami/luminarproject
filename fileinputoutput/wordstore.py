f=open("words","r")
words=[]
for lines in f:
    line=lines.rstrip("\n")
    word=line.split(" ")
for wrd in words:
    words.append(wrd)
print(word)
