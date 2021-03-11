//words split

var text="hello hai hello hai"
var words=text.split(" ")
var dict={}
for(var word of words){
if(word in dict){
dict[word+=1]
}
else{
dict[word]=1
}
}
console.log(dict)
