let clk=document.querySelector("#clk")
function clikedfn(){
clk.style.color="red";
clikedfn.textContent="cliked on me"
}
clk.addEventListener("click",clikedfn)

let dbl=document.getElementById("dbl")
dbl.addEventListener("dblclick",()=>{
dbl.style.color="green";
dbl.textContent="dblclicked"

})
let hov=document.querySelector("#hov")
hov.addEventListener("mouseover",()=>{
hov.style.color="cyan"
hov.textContent="mouseoverme"
})

hov.addEventListener("mouseout",()=>{
hov.textContent="mouse not over me";
hov.style.color="red";
})

