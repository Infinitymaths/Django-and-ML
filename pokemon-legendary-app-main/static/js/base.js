const btn=document.getElementById("btn");
const menu=document.querySelector(".menu");

btn.addEventListener("click",()=>{
    if(btn.checked==true){
        menu.classList.add("active");
    }
    else{
        menu.classList.remove("active");
    }
});