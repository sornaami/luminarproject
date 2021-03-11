let employee=[{eid:100,name:"ajay",desig:"devop",join:1981,resign:2003},
{eid:101,name:"vijay",desig:"devop",join:1992,resign:2008},
{eid:102,name:"bijoy",desig:"ba",join:1999,resign:2007},
{eid:103,name:"jhon",desig:"ba",join:1989,resign:2010},
{eid:104,name:"danie",desig:"qa",join:2009,resign:2014},
{eid:105,name:"lari",desig:"qa",join:1987,resign:2010}
]
//emp name and desig
for(let emp of employee){
console.log(emp.name+","+emp.desig)
}
 // desig=devops,name
var employ=employee.filter(emp=>(emp.desig)=='devop')
console.log(employ)
    //working in 80 details
var employe=employee.filter(emp=>(emp.join)>1980 && (emp.join)<1990)
console.log(employe)
    //have exp 9 years
var empl1=employee.filter(emp=>(emp.resign)-(emp.join)>9)
console.log(empl1)
    //sort based on joining year
var empl=employee.sort((emp1,emp2)=>(emp1.join)>(emp2.join)?1:1)
console.log(empl)




