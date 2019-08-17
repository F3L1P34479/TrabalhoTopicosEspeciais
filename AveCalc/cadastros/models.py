from django.db import models

# Create your models here.
#toda classe no django é um model
class Estado(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    sigla   = models.CharField(max_length=2, unique = True)
    nome    = models.CharField(max_length=50)

    #Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    #Quando você tem uma palavra toda em maiuscula significa que ela é uma constante
    nome        = models.CharField(max_length=50)
    estado      = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao   = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição",
        help_text="Espaço para colocar qualquer informação."
        )

    def __str__(self):
        return self.nome + " - " + self.estado.sigla


class Pessoa(models.Model):
    nome        = models.CharField(max_length=100, help_text="Digite seu nome completo")
    nascimento  = models.DateField(verbose_name="Data de nascimento")
    email       = models.EmailField(max_length=100, help_text="Digite seu e-mail")
    cidade      = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)

class Racao(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    sigla   = models.CharField(max_length=2, unique = True)
    nome    = models.CharField(max_length=80)

    #Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome

class Matriz(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    idade   = models.CharField(max_length=2, unique = True)
    nome    = models.CharField(max_length=50)

    #Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome
