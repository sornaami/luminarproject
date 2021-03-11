class Student{
  setStudent(name,rollno,course,total){
  this.name=name;
  this.rollno=rollno;
  this.course=course;
  this.total=total;
  }
  printStudent(){
  console.log(this.name)
  console.log(this.rollno)
  console.log(this.course)
  console.log(this.total)
  }
}
var obj=new Student()
obj.setStudent("samvi",25,"eng",500)
obj.printStudent()