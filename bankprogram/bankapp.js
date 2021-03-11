class MyBank{
Static getUserData(){
var users={
userone:{username:"userone",password:"userone",acno:1000,balance:5000},
usertwo:{username:"usertwo",password:"usertwo",acno:1001,balance:1000},
userthree:{username:"userthree",password:"userthree",acno:1002,balance:8000}
}
return users
}
Static login(){
let uname=document.querySelector("#uname").value
let pasword=document.querySelector("#pwd").value
let users=MyBank.getUserData()
if(unmae in users){
  if(pasword=users[uname]["password"]){
  alert("login sucess")
  window.location.href="userhome.html"
  }
  else{
  alert("invalid password")
}
else{
alert("there is no user")}
}
}
}

static deposit(){
let uname=document.querySelector("#uname").value
let amt=Number(document.querySelector("#amount").value)
var users=MyBank.getUserData()
if(uname in users){
users[uname]["balance"]+=amt
alert(users[uname]["balance"])
}
else{
alert("invalid credentials")
}
}
static withdraw{
let uname=document.querySelector("#uname").value
let amt=Number(document.querySelector("#amount").value)
var users=MyBank.getUserData()
if(uname in users){
if(amt>users[uname]["balance"])
alert("insufficient balance")
}
else{
users[uname]["balance"]-=amt
alert(users[uname]["balance"])
}
else{
alert("invalid credentials")
}
}

}