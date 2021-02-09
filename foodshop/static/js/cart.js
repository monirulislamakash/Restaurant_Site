var addToCat=document.querySelectorAll("#cartadd");
var idcatcher=document.getElementById('contaty');
var allprice=0;
var foodname=[]
var contaty=0;
addToCat.forEach((idpicer)=>{
    idpicer.addEventListener('click',()=>{
        foodname.push(idpicer.dataset.name);
        allprice+=Number(idpicer.dataset.price);
        contaty+=1;
        idcatcher.innerHTML=contaty;
    });
})