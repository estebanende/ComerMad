var projectsImg = document.getElementsByClassName("carousel__slide");

let ventanas_abiertas = null;
for (const img of projectsImg) {
    img.addEventListener("click", function() {
        var img_seleccionada = this.querySelector("img");
        console.log(ventanas_abiertas);
        if (ventanas_abiertas != null && !ventanas_abiertas.closed) {
            ventanas_abiertas.close();
          
        }
        ventanas_abiertas = window.open(img_seleccionada.src, "ImagenModal", "width=800,height=600");
    });
}
