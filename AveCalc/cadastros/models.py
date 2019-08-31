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
    #descricao   = models.TextField(
        #blank=True,
        #null=True,
        #verbose_name="Descrição",
        #help_text="Espaço para colocar qualquer informação."
        #)

    def __str__(self):
        return self.nome + " - " + self.estado.sigla


class Pessoa(models.Model):
    nome        = models.CharField(max_length=100, help_text="Digite seu nome completo")
    #nascimento  = models.DateField(verbose_name="Data de nascimento")
    email       = models.EmailField(max_length=100, help_text="Digite seu e-mail")
    #cidade      = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    fone        = models.CharField(max_length=15, help_text="Digite seu telefone", verbose_name="Telefone")

    def __str__(self):
        return self.nome + ' - ' + self.fone

class Racao(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    sigla   = models.CharField(max_length=4, unique = True)
    nome    = models.CharField(max_length=80)

    #Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome

class Entrada(models.Model):
    #Quando você tem uma palavra toda em maiuscula significa que ela é uma constante
    dataChegada        = models.DateField()
    peso               = models.PositiveIntegerField(max_length=5, unique = True)
    racao              = models.ForeignKey(Racao, on_delete=models.PROTECT)

    def __str__(self):
        return self.peso + " - " + self.racao.sigla

class Matriz(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    idade   = models.CharField(max_length=2, unique = True)
    loteMatriz    = models.CharField(max_length=50)

    #Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome

class Aviario(models.Model):
    #nome_do_atributo = models.Tipo(configuração)
    identificacao          = models.CharField(max_length=10, verbose_name = "Identificação")
    localizacao            = models.CharField(max_length=100, verbose_name = "Localização")
    cidade                 = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    largura                = models.PositiveIntegerField()
    comprimento            = models.PositiveIntegerField()
    capacidadeAlojamento   = models.PositiveIntegerField(verbose_name = "Capacidade de Alojamento")
    ventilacao             = models.CharField(max_length=50, verbose_name = "Tipo de ventilação")

    #Como se fosse toString e self = this
    def __str__(self):
        return self.identificacao + ' - ' + str(self.capacidadeAlojamento)
