from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    CPF = models.CharField(max_length=11) # TODO acionar validador de CPF e concatenação
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Casa(models.Model):
    dono = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_suites = models.IntegerField()
    qtd_quartos = models.IntegerField()
    qtd_banheiros = models.IntegerField()
    cep = models.CharField(max_length=8) # TODO acionar validador de cep
    rua = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    descricao = models.TextField()
    
    def __str__(self):
        return f'R${self.valor}, Suite(s): {self.qtd_suites} Quarto(s): {self.qtd_quartos}'