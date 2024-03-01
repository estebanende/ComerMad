
menuspan=document.getElementsByClassName("MenuSpan")
menuFlotannte=document.getElementById("MenuHamburger").addEventListener("click",function(){

    let menu = document.querySelector(".menuFlotante");
    menu.classList.toggle("active");
    let MenuHamburger=document.querySelector("#MenuHamburger");
    console.log(MenuHamburger)
    MenuHamburger.classList.toggle("active")
    
})
let ventanaabierta=null
let ventanaPrincipal=document.body
clickEnfotos=document.getElementsByClassName("Imagen_Prodcutos")
for (const iterator of clickEnfotos) {
    
    iterator.addEventListener("click",function () {
        
        console.log(ventanaabierta)
        if(ventanaabierta!=null){
         ventanaabierta.close()
        }
        ventanaabierta=window.open(iterator.src, "_blank", "width=800,height=600");
       
    })
}
