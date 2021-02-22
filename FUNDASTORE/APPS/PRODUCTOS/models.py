from django.db import models

# Create your models here.
class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=128)
    cat_itbms = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.cat_nombre

class Producto(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_nombre = models.CharField(max_length=128)
    pro_precio = models.DecimalField(max_digits=8,decimal_places=2)
    pro_stock = models.IntegerField()
    pro_descripcion = models.TextField(null=True)
    pro_categoria = models.ForeignKey(to=Categoria,on_delete=models.CASCADE,null=True)
    pro_imagen = models.ImageField(upload_to='PRODUCTOS',max_length=128,default='default.png')

    def __str__(self):
        return self.pro_nombre