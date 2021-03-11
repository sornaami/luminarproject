class Person{
  constructor(age,name){
  this.age=age;
  this.name=name;
  }
  printPerson(){
  console.log(this.age)
  console.log(this.name)
  }
 }
//object
var obj=new Person(25,"ajay")
obj.printPerson()
//setPerson perform initializing instance variable
//constructor intialize instance variable