from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name = "Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edicion")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    contet = RichTextField(verbose_name = "Contenido")
    publish = models.DateTimeField(verbose_name = "Fecha de publicacion", default = now)
    image = models.ImageField(verbose_name = "Imagen", upload_to = "Blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name = "Autor", on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = "Categorias", related_name="get_posts")

    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edicion")

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
