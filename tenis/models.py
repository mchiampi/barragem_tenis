from django.db import models

# Create your models here.

class Rodada(models.Model):
    nome = models.CharField(max_length=30)
    ano = models.DateTimeField('ano da rodada')
    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    tel_celular = models.CharField(max_length=20)
    tel_casa = models.CharField(max_length=20)
    tel_trabalho = models.CharField(max_length=20)
    correio_eletronico = models.CharField(max_length=50)
    status_jogador = models.CharField(max_length=15)
    def __str__(self):
        return self.apelido

class Jogo(models.Model):
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    #desafiado = models.CharField(max_length=30)
    #desafiante = models.CharField(max_length=30)
    desafiado = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='desafiados')
    desafiante = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='desafiantes')
    data = models.DateTimeField('data')
    #hora = models.DateTimeField('hora')
    games_1set_desafiado = models.IntegerField(default=0)
    games_1set_desafiante = models.IntegerField(default=0)
    games_2set_desafiado = models.IntegerField(default=0)
    games_2set_desafiante = models.IntegerField(default=0)
    games_3set_desafiado = models.IntegerField(default=0)
    games_3set_desafiante = models.IntegerField(default=0)
    def __str__(self):
        return '{self.desafiado} X {self.desafiante}'.format(self=self)
