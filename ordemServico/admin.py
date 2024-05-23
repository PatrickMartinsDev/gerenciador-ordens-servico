from django.contrib import admin

from .models import Cadastro, Carro, OrdemServico

admin.site.register(Cadastro)
admin.site.register(Carro)
admin.site.register(OrdemServico)