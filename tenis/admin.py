from django.contrib import admin

# Register your models here.
from .models import Rodada, Jogador, Jogo
admin.site.register(Rodada)
admin.site.register(Jogador)
admin.site.register(Jogo)
