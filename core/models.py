from django.db import models

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE)
    plataformas = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.nome