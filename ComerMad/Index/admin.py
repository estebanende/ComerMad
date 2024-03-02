from django.contrib import admin
from .models import Model_Cahppa,Cahppa

# Register your models here.
class RegisdtrarChapas(admin.ModelAdmin):
    fields=["id","Type_Style","description"]
    list_display=["id","Type_Style","description"]

admin.site.register(Model_Cahppa, RegisdtrarChapas)


class FormsdminView(admin.ModelAdmin):
    # Especifica la plantilla a usar para esta vista personalizada
    fields=["name","id_Type_Style","colur","provider","imagen","description"]
    list_display=["name","id_Type_Style","colur","provider","imagen","description"]
# Registra el modelo con la vista personalizada en el administrador
admin.site.register(Cahppa, FormsdminView)