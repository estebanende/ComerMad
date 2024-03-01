from django import forms
from .models import Cahppa, Model_Cahppa

from django import forms
from .models import Cahppa, Model_Cahppa

class ProductoForm(forms.ModelForm):
    id_Type_Style = forms.ModelChoiceField(
        queryset=Model_Cahppa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',  # Utiliza el campo 'name' como valor de la opción
        label='Type Style'
    )

    class Meta:
        model = Cahppa
        fields = ['name', 'id_Type_Style','description' ,'colur', 'provider', 'imagen']
        
class SendFormulario(forms.Form):
           nombre=forms.CharField(max_length=200)
           correo=forms.EmailField()
           mensaje=forms.CharField(widget=forms.Textarea)
    
