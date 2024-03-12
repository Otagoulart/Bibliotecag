from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Cidade)
admin.site.register(Usuario)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Genero)