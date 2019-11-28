from django.db import models

# Create your models here.

class Catalogo(models.Model):
    supermercado = models.CharField(max_length = 20)
    sku = models.CharField(max_length = 20)
    articulo = models.CharField(max_length = 200)
    precio = models.CharField(max_length=20, default = 0)
    url_img = models.CharField(max_length = 200)
    oferta = models.CharField(max_length = 100, blank= True)
