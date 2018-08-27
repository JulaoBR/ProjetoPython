from django.db import models

class Funcionario(models.Model):

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):

    descricao = models.CharField(
       max_length=100,
       null=False,
       blank=False 
    )

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):

    descricao = models.CharField(
       max_length=100,
       null=False,
       blank=False 
    )

    def __str__(self):
        return self.descricao

'''
    class Teste(models.Model):
        //campo data decimal
        valor = models.DecimalField(max_digits=7, decimal_places=2)

        //faz relacionamento entre tabelas
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE),

        class Metsa:
            varbose_name_plural = 'Transações'
'''