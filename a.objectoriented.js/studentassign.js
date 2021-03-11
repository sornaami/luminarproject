class Student{
constructor(rollno,name,total,course){
this.rollno=rollno
this.name=name
this.total=total
this.course=course
}
printStudent(){
console.log(this.rollno)
console.log(this.name)
console.log(this.total)
console.log(this.course)
}
}
var obj=new Student(11,"anu","eng",400)
var obj1=new Student(12,"reji","bca",120)
var obj2=new Student(13,"samvi","bca",150)
var obj3=new Student(14,"siva","bba",200)
var obj4=new Student(15,"vinu","Mca",100)

obj.printStudent()
obj1.printStudent()
obj2.printStudent()
obj3.printStudent()
obj4.printStudent()

var arr=[]

arr.push(obj)
arr.push(obj1)
arr.push(obj2)
arr.push(obj3)
arr.push(obj4)

for (var stud of arr){
console.log(stud)
}



//print student course bba
var studen=arr.filter(Stud=>stud.course=="bba")
console.log(studen)
//total>135
var tot=arr.map(obj=>obj.total).reduce((obj,obj1)=>obj+obj1)
console.log(tot)
// students with high
var high=arr.map(obj=>obj.total).reduce((obj,obj1)=>obj>obj?obj:obj1)
console.log(high)
//total
var srt=arr.sort((obj,obj1)=>obj.total>obj1.total?-1:1)
console.log(srt)
