from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Cahppa,Model_Cahppa
from .forms import ProductoForm,SendFormulario
from django.contrib import messages
from django.template import loader
from django.core.mail import send_mail
from email.message import EmailMessage
from django.shortcuts import get_object_or_404

# Create your views here.
def binvenido(request):
    print("llego aquí a la función sendMail")
    if request.method == 'POST':
        form = SendFormulario(request.POST)
        if form.is_valid():
            try:
                    print("estoy entrando or aquí?")
                    nombre = form.cleaned_data['nombre']
                    destinatario = form.cleaned_data['correo']
                    mensaje = form.cleaned_data['mensaje']

                    # Utiliza la función send_mail de Django
                    send_mail(
                        'Asunto del Correo',
                        mensaje,
                        'estebanignaci6@gmail.com',  # Remitente
                        [destinatario],  # Destinatario
                        fail_silently=False,  # Puedes cambiar a True para evitar que se levante una excepción en caso de error
                    )

                    # Puedes redirigir a una página de éxito o hacer lo que necesites
                    return render(request, 'exito.html', {'nombre': nombre})
            except Exception as e:
                print(e)
    else:
        form = SendFormulario()
        print("llego aquí a la función sendMail por el else?")

    return render(request, 'index.html', {'form': form})
    
       
      
       
def adios(request,id_typpe_chappa):
    categoria=request.GET.get('categoria')
    
    print("***********------------*************")
    print(categoria)
    print(id_typpe_chappa)
    if categoria==None or categoria==id_typpe_chappa:
        print("le acabamos de dar al filtrar")
        objectChapas=Cahppa.objects.filter(id_Type_Style=id_typpe_chappa)
    else:
        objectChapas=Cahppa.objects.filter(name__contains=categoria)
    
    templates=loader.get_template('Product.html')
    tipochapa=get_object_or_404(Model_Cahppa,id=id_typpe_chappa)
    
    context={
        'id_chapa':id_typpe_chappa,
        'product':objectChapas,
        'nombre':tipochapa
    }

    print(objectChapas)
    
    return HttpResponse(templates.render(context, request))


def crear_producto(request):
    if request.method == 'POST':
        print("entro por aqui  soy post:")
        print(request)
        form = ProductoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'se ha creado el empaque exitosamente')
            return render(request, 'crear_producto.html', {'form': form})  # Cambia 'lista_productos' por el nombre de tu vista de lista de productos
    else:
        form = ProductoForm()
        print("entro por aqui no soy post:")
        print(request)

    return render(request, 'crear_producto.html', {'form': form})


def descriptionChapa (request,nameChapa):
    print(nameChapa)
    chappaFind=get_object_or_404(Cahppa,name=nameChapa)
    print('***/***/****')
    templates=loader.get_template('Description_product.html')
    context={
        'ChappaFind':chappaFind
    }
    print(chappaFind.imagen)
    return HttpResponse(templates.render(context, request))


    
#http://127.0.0.1:8000/index.html/Product.html/1