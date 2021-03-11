var htags=document.getElementsByTagName("h1")
for(let tags of htags){
tags.style.color="red";
}
var lst=document.getElementsByTagName("li")
for(let tags of lst){
tags.style.color="green";
}
//let hone=document.getElementById("hone")
//hone.style.color="blue";

var cls=document.getElementsByClassName("lt")
for(let tags of cls){
tags.style.color="yellow";
}
//let qsl=document.querySelectorAll("li")
//for(let tags of qsl){
//tags.style.color="red";
//}
//let hone=document.querySelectorAll("h1)
//for(let tags of hone){
//tags.style.color="cyan";
//}

//let htwo=document.querySelectorAll("#hone")
//htwo.style.color="red"

//let qsa=document.querySelectorAll(".lt")
//for(let tags of qsa){
//tags.style.color="blue";
//}

//let hone=document.querySelector("#hone")
//let data=hone.textcontent
//alert(data)
hone.textContent="Welcome To DOM"
let lstem=document.querySelectorAll(".lt")
for(let val of lstem){
val.innerHTML="<em>listitem</em>"
}


