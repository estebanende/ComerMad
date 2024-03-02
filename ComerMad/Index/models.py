from django.db import models

# Create your models here.



class Model_Cahppa(models.Model):
    id=models.BigIntegerField(primary_key=True)
    Type_Style=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    


#sin esto me sale el object porque no sabe que coger como nombre
    
    def __str__(self):
        return self.description
    
class Cahppa(models.Model):
    name=models.CharField(max_length=300,primary_key=True)
    id_Type_Style=models.ForeignKey(Model_Cahppa,on_delete=models.CASCADE)
    colur=models.CharField(max_length=100)
    provider=models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    description=models.TextField(max_length=200,null=True)
