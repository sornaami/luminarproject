function add(num1,num2){
return num1+num2
}

var f=(num1,num2)=>num1+num2
console.log(f(10,50))

//cube
var cube=num=>num**3
console.log(cube(3))

//map

var arr=[2,3,4,5,6]
var squares=arr.map(num=>num**2)
console.log(squares)

//filter
var evens=arr.filter(num=>num%2==0)
console.log(evens)

var arr=[10,11,2,3,4,5,6]
var sorted=arr.sort(num1,num2)=>num1-num2
console.log(sorted)


//reduce
var total=arr.reduce(num1,num2)=>num1+num2
console.log(total)

var maximum=arr.reduce((num1,num2)=>num1>num2?num1:num2)
console.log(maximum)





